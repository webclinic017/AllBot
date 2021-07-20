from app.backtest.ManagerBacktest import *
from flask import Blueprint, request
import json

backtest_blueprint = Blueprint('backtest_blueprint', __name__)


@backtest_blueprint.route('/backtest', methods=['GET'])
def backtest():
    data = json.loads(request.data)
    return getBacktest(data)

