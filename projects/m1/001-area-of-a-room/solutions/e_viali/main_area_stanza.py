
def inserisci_float(prompt):
    ok = False
    while not ok:
        try:
            val =  input(prompt)
            float_val = float(val)
            return float_val
        except:
            ok = False
            print(f"inserito valore non numerico: {val}")


def calcola_area(larghezza: float , lunghezza: float) -> float:
    assert(type(larghezza) == int or float)
    assert(type(lunghezza) == int or float)
    return larghezza*lunghezza


if __name__ == "__main__":

    def main():
        lunghezza = inserisci_float("Inserire la lunghezza: ")
        larghezza = inserisci_float("Inserire la larghezza: ")
        area = round(calcola_area(larghezza,lunghezza), 2)
        print (f"L'area della stanza di lunghezza {lunghezza} e larghezza {larghezza} è : mq {area}")

    main()