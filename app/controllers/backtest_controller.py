from app.services.BackTestService import getOneBackTest, getAllBackTest
from flask import Blueprint, request

backtest_blueprint = Blueprint('backtest_blueprint', __name__)


@backtest_blueprint.route('/backtest', methods=['GET'])
def oneBacktest():
    return getOneBackTest(request.json)

@backtest_blueprint.route('/backtests', methods=['GET'])
def allBacktest():
    return getAllBackTest(request.json)


