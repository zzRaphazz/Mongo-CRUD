from database.usuario.usuarioDelete import usuarioDelete
from bson.objectid import ObjectId

def usuarioDeleteMenu():
    id = input("ID do usuario: ")

    if id == "":
        print()
        print("ID não pode ser vazio!")
        input()
        return

    filtro = {
        "_id": ObjectId(id)
    }

    usuarioDelete(filtro)
    input()