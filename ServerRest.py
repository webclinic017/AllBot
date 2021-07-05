from flask import Flask
from service.RobotController import robots_blueprint
from service.ManagerRobotsController import managerRobots_blueprint
from service.BacktestController import backtest_blueprint

app = Flask(__name__)
app.register_blueprint(robots_blueprint)
app.register_blueprint(managerRobots_blueprint)
app.register_blueprint(backtest_blueprint)
app.secret_key = "super secret key"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
