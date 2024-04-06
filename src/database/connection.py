import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("<sua_conexao>", server_api=ServerApi('1'))
database = client.MercadoLivre
