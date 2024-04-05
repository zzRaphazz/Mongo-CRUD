from database.compra.compraRead import compraRead, compraReadAll

def compraReadMenu():
    filtro = {
        "data": str(input("Digite uma data: ")).lower()
    }

    if filtro["data"] == "":
        compraReadAll()
    else:
        compraRead(filtro)