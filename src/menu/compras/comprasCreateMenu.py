import datetime


def comprasCreateMenu():
    
    # Data
    data_compra = str(input("Digite a data da compra: (dd/mm/aaaa) "))
    data_compra = data_compra.lower().split("/")
    try:
        data_compra = datetime.datetime(int(data_compra[2]), int(data_compra[1]), int(data_compra[0]))
    except:
        print()
        print("Data inválida!")
        input()
        return

    compra ={
        "usuario": {},
        "produtos": [
            {}
        ],
        "data_compra": data_compra,
        "valor_total": 0
    }

    print(compra)

    input()