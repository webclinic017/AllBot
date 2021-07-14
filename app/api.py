from flask import Flask
from .service.RobotController import robots_blueprint
from .service.ManagerRobotsController import managerRobots_blueprint
from app.service.BacktestController import backtest_blueprint
from .database import Connection


def create_app(config_object="app.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    Connection.init_app(app.config["Bots"], app.config['MONGO_URI'])
    app.register_blueprint(robots_blueprint)
    app.register_blueprint(managerRobots_blueprint)
    app.register_blueprint(backtest_blueprint)
    return app

