from celery import Celery
from Database import connection
from Schemas import BackTestSchema, RankingSchema, RobotSchema
from ManagerBacktest import getRanking, getBacktest
from settings import *
from bson import ObjectId
from datetime import datetime

app = Celery('tasks', broker=CELERY_BROKER_URL)

print(CELERY_BROKER_URL)


@app.task()
def runRanking():
    ranking = RankingSchema.objects().first()
    if ranking is None:
        ranking = RankingSchema()
    if (datetime.now() - ranking.lastUpdate).total_seconds() > 14400:
        ranking.stats = getRanking()
        ranking.lastUpdate = datetime.now()
        ranking.save()


@app.task()
def runBackTest(id):
    robotSchema = RobotSchema.objects(id=ObjectId(id)).first()
    if robotSchema:
        comb = robotSchema.comb()
        backtest = BackTestSchema.objects(comb=comb).first()
        if (backtest is None) or ((datetime.now() - backtest.lastUpdate).total_seconds() > 14400):
            stats = getBacktest(robotSchema)
            if backtest:
                backtest.update(stats=stats, lastUpdate=datetime.now())
            else:
                backtest = BackTestSchema()
                backtest.comb = comb
                backtest.stats = stats
                backtest.lastUpdate = datetime.now()
                backtest.save()
