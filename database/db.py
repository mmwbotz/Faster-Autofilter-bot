from pymongo import MongoClient  
from info import DATABASE_URI

mongo_client = MongoClient(DATABASE_URI)
db = mongo_client['hehe']  
users = db['users']
