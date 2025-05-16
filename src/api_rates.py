import requests

def obtenir_taxes(base="EUR"):
    """
    Aquesta funció obté les taxes de conversió en temps real de la moneda base especificada.
    Retorna un diccionari amb les taxes per a 'EUR', 'USD' i 'GBP'.
    """
    api_key = "b3faf4da6d641767bdeed460"

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
    
    try:
        resposta = requests.get(url)

        if resposta.status_code != 200:
            print("Error en la petició. Codi d'estat:", resposta.status_code)
            return None
        
        dades = resposta.json()

        if dades.get("result") != "success":
            print("Error en l'API:", dades.get("error-type", "Desconegut"))
            return None
        
        taxes = dades.get("conversion_rates", {})

        resultats = {
            "EUR": taxes.get("EUR"),
            "USD": taxes.get("USD"),
            "GBP": taxes.get("GBP")
        }

        return resultats
    
    except requests.exceptions.RequestException as e:
        print("Excepció durant la petició:", e)
        return None
    
if __name__ == "__main__":
    resultats = obtenir_taxes("EUR")
    if resultats:
        print("Taxes en temps real basades en EUR:")
        print("De EUR a EUR:", resultats["EUR"])
        print("De EUR a USD:", resultats["USD"])
        print("De EUR a GBP:", resultats["GBP"])
    else:
        print("No s'han pogut obtenir les dades.")
