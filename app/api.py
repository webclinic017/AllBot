from app.controllers.RobotController import robots_blueprint
from app.controllers.ManagerRobotsController import managerRobots_blueprint
from app.controllers.BacktestController import backtest_blueprint
from app.database import Connection
from flask import Flask
from binance.lib.utils import config_logging
import logging


def create_app(config_object="app.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    Connection.init_app(app.config["DB"], app.config['MONGO_URI'])
    config_logging(logging, logging.DEBUG)
    app.register_blueprint(robots_blueprint)
    app.register_blueprint(managerRobots_blueprint)
    app.register_blueprint(backtest_blueprint)
    return app

