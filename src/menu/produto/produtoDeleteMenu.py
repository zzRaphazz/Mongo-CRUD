from database.produto.produtoDelete import produtoDelete
from bson.objectid import ObjectId

def produtoDeleteMenu():

    id = input("ID do produto: ")

    if id == "":
        print()
        print("ID não pode ser vazio!")
        input()
        return

    filtro = {
        "_id": ObjectId(id)
    }
    
    produtoDelete(filtro)
    input()