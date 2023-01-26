from settings import DB, MONGO_URI
from mongoengine import connect


connection = connect(db=DB, host=MONGO_URI)
