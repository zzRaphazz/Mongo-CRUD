from database.compra.compraRead import compraRead, compraReadAll
import datetime

def compraReadMenu():
    data = str(input("Digite uma data: ")).lower()

    if data == "":
        compraReadAll()
        return

    data = data.lower().split("/")
    try:
        data = datetime.datetime(int(data[2]), int(data[1]), int(data[0]))
    except:
        print()
        print("Data inválida!")
        input()
        return
    
    print(data)

    filtro = {
        "data_compra": data
    }

    compraRead(filtro)