from celery import Celery
from celery.schedules import crontab
from Database import connection
from Schemas import BackTestSchema, RankingSchema, RobotSchema
from ManagerBacktest import getRanking, getBacktest
from bson import ObjectId

app = Celery('tasks',
             broker='redis://:Sg2oKCcsul4L6yJdgunwM6JP7MPiSXYP@redis-12481.c270.us-east-1-3.ec2.cloud.redislabs.com:12481/0')

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'worker.runAllBacktests',
        'schedule': 30.0,
        'args' : ()
    },
}
app.conf.timezone = 'UTC'


@app.task()
def runRanking():
    ranking = RankingSchema.objects().first()
    if ranking is None:
        ranking = RankingSchema()
    ranking.stats = getRanking()
    ranking.save()


@app.task()
def runBackTest(id):
    robotSchema = RobotSchema.objects(id=ObjectId(id)).first()
    if robotSchema:
        stats, comb = getBacktest(robotSchema)
        backtest = BackTestSchema.objects(comb=comb).first()
        if backtest:
            backtest.update(stats=stats)
        else:
            backtest = BackTestSchema()
            backtest.comb = comb
            backtest.stats = stats
            backtest.save()
