from mongoengine import connect
from settings import *

connection = connect(db=DB, host=MONGO_URI)


