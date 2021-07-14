from mongoengine import connect

connection = None


def init_app(db, host):
    global connection
    connection = connect(db=db, host=host)
