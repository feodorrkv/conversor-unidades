from src.input_output import mostrar_menu, obtenir_entrada
from src.conversion import (
    convertir_moneda,
    convertir_temperatura,
    convertir_distancia,
    convertir_pes,
    convertir_volum
)
from src.utils import registrar_conversion_csv

def main():
    print("=== Conversor d'Unitats ===")
    categoria = mostrar_menu()
    valor, unitat_origen, unitat_destí = obtenir_entrada(categoria)

    if categoria == "moneda":
        resultat = convertir_moneda(valor, unitat_origen, unitat_destí)
    elif categoria == "temperatura":
        resultat = convertir_temperatura(valor, unitat_origen, unitat_destí)
    elif categoria == "distància":
        resultat = convertir_distancia(valor, unitat_origen, unitat_destí)
    elif categoria == "pes":
        resultat = convertir_pes(valor, unitat_origen, unitat_destí)
    elif categoria == "volum":
        resultat = convertir_volum(valor, unitat_origen, unitat_destí)
    else:
        print("Categoría no reconeguda.")
        return

    if resultat is not None:
        print(f"Resultat de la conversió: {resultat:.2f}")
        registrar_conversion_csv(categoria, valor, unitat_origen, unitat_destí, resultat)
    else:
        print("No s'ha pogut realitzar la conversió.")

if __name__ == "__main__":
    main()