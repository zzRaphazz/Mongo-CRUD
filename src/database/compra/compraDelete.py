from database.connection import database

def compraDelete(filtro):
    global database
    
    print()
    compra = database.compra.find_one(filtro)
    if compra == None:
        print("Compra não encontrada")
        return
    else:
        database.compra.delete_one(filtro)
        print(f"Compra {compra['_id']} deletada")