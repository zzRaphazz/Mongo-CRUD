from database.vendedor.vendedorDelete import vendedorDelete
from bson.objectid import ObjectId

def vendedorDeleteMenu():
    id = input ("ID do vendedor: ")

    if id == "":
        print()
        print("ID não pode ser vazio!")
        input()
        return
    
    filtro = {
        "_id": ObjectId(id)
    }

    vendedorDelete(filtro)
