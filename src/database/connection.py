import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb://localhost:27017", server_api=ServerApi('1'))
database = client.TesteSRC
