from flask import Blueprint, request
import json

backtest_blueprint = Blueprint('backtest_blueprint', __name__)


@backtest_blueprint.route('/backtest', methods=['GET'])
def backtest():
    return getBacktest(json.loads(request.data)), 200

