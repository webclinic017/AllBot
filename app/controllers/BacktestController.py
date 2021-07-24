from app.services.BackTestService import getOneBackTest
from flask import Blueprint, request

backtest_blueprint = Blueprint('backtest_blueprint', __name__)


@backtest_blueprint.route('/backtest', methods=['GET'])
def oneBacktest():
    return getOneBackTest(request.json)

