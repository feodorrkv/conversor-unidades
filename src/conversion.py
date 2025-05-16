from src.api_rates import obtenir_taxes

def convertir_moneda(valor, origen, destí):
    taxes = obtenir_taxes(origen)
    if taxes is None:
        print("No s'ha pogut obtenir la taxa actual.")
        return None
    factor = taxes.get(destí)
    if not factor:
        print("La taxa per a la moneda especificada no està disponible.")
        return None
    return valor * factor
    
def convertir_temperatura(valor, origen, destí):
    if origen == destí:
        return valor
    if origen == "Celsius":
        temp_c = valor
    elif origen == "Fahrenheit":
        temp_c = (valor - 32) * 5/9
    elif origen == "Kelvin":
        temp_c = valor - 273.15
    else:
        print("Unitat d'origen no vàlida.")
        return None
    
    if destí == "Celsius":
        return temp_c
    elif destí == "Fahrenheit":
        return (temp_c * 9/5) + 32
    elif destí == "Kelvin":
        return temp_c + 273.15
    else:
        print("Unitat destí no vàlida.")
        return None
    
def convertir_distancia(valor, origen, destí):
    factors = {
        "metres": 1.0,
        "quilòmetres": 1000.0,
        "milles": 1609.34
    }
    try:
        metres = valor * factors[origen]
        resultat = metres / factors[destí]
        return resultat
    except KeyError:
        print("Unitats de distància no vàlides.")
        return None
    
def convertir_pes(valor, origen, destí):
    factors = {
        "grams": 1.0,
        "kilograms": 1000.0,
        "libras": 453.592
    }
    try:
        grams = valor * factors[origen]
        resultat = grams / factors[destí]
        return resultat
    except KeyError:
        print("Unitats de pes no vàlides.")
        return None
    
def convertir_volum(valor, origen, destí):
    factors = {
        "litres": 1.0,
        "mil·lilitres": 0.001,
        "gallons": 3.78541
    }
    try:
        litres = valor * factors[origen]
        resultat = litres / factors[destí]
        return resultat
    except KeyError:
        print("Unitats de volum no vàlides.")
        return None