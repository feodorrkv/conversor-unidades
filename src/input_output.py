def mostrar_menu():
    print("Escull la magnitud a convertir:")
    print("1 - Moneda")
    print("2 - Temperatura")
    print("3 - Distància")
    print("4 - Pes")
    print("5 - Volum")
    eleccio = input("Introdueix el número corresponent (1-5): ")
    magnituds = {
        "1": "moneda",
        "2": "temperatura",
        "3": "distància",
        "4": "pes",
        "5": "volum"
    }
    return magnituds.get(eleccio, "moneda")

def obtenir_entrada(categoria):
    if categoria == "moneda":
        unitats = ["EUR", "USD", "GBP"]
    elif categoria == "temperatura":
        unitats = ["Celsius", "Fahrenheit", "Kelvin"]
    elif categoria == "distància":
        unitats = ["metres", "quilòmetres", "milles"]
    elif categoria == "pes":
        unitats = ["grams", "kilograms", "libras"]
    elif categoria == "volum":
        unitats = ["litres", "mil·lilitres", "gallons"]
    else:
        unitats = []

    print(f"Unitats disponibles per a {categoria}: {', '.join(unitats)}")
    unitat_origen = input("Introdueix la unitat d'origen: ")
    unitat_destí = input("Introdueix la unitat destí: ")
    
    while True:
        try:
            valor = float(input("Introdueix el valor a convertir: "))
            break
        except ValueError:
            print("Si us plau, introdueix un valor numèric.")
    
    return valor, unitat_origen, unitat_destí