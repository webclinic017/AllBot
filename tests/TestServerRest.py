from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return {"data": str(datetime.now())}


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
