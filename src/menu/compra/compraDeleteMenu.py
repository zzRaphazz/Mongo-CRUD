from bson.objectid import ObjectId
from database.compra.compraDelete import compraDelete

def compraDeleteMenu():
    id = input("ID da compra: ")

    if id == "":
        print()
        print("ID não pode ser vazio!")
        input()
        return

    filtro = {
        "_id": ObjectId(id)
    }

    compraDelete(filtro)
    input()
