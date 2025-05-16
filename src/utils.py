import csv
from datetime import datetime
import os

def registrar_conversion_csv(categoria, valor, unitat_origen, unitat_destí, resultat):
    """
    Registra una conversió en el fitxer CSV 'historial.csv'.
    Guarda les següents dades:
      - Data/Hora
      - Magnitud (ex.: moneda, temperatura, etc.)
      - Valor (valor introduït)
      - Unitat Origen
      - Unitat Destí
      - Resultat (valor resultant de la conversió)
    """
    filename = "historial.csv"

    file_exists = os.path.isfile(filename)
    
    try:
        with open(filename, mode="a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            if not file_exists:
                header = ["Data/Hora", "Magnitud", "Valor", "Unitat Origen", "Unitat Destí", "Resultat"]
                writer.writerow(header)

            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            fila = [data_hora, categoria, valor, unitat_origen, unitat_destí, resultat]
            writer.writerow(fila)

            print("Conversió registrada correctament en el fitxer CSV.")
    except IOError as error:
        print("Error escrivint en el fitxer CSV:", error)