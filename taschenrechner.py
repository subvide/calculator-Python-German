
zahl_1 = 0
zahl_2 = 0

def check_operation(zahl_1, operation):
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        zahl_2 = int(input("Zweite Zahl: "))
        ergebnis = rechnung(zahl_1, zahl_2, operation)
        return ergebnis
    else:
        print("Bitte gültige Rechenoperation eingeben.")
        start(zahl_1)

def start(zahl_1):
    while True:
        operation = input("Operation (+,-,*,/ oder 'x' zum abbrechen): ")
        if operation == "x":
            print("Taschenrechner beendet.")
            exit()
        else:
            new_ergebnis = check_operation(zahl_1, operation)
            print(f"Dein neustes Ergebnis ist {new_ergebnis}.")
            zahl_1 = new_ergebnis

def rechnung(zahl_1, zahl_2, operation):
    match operation:
        case "+":
            ergebnis = zahl_1 + zahl_2
        case "-":
            ergebnis = zahl_1 - zahl_2
        case "*":
            ergebnis = zahl_1 * zahl_2
        case "/":
            ergebnis = zahl_1 / zahl_2
    return ergebnis

def main():
    zahl_1 = int(input("Erste Zahl: "))
    start(zahl_1)

main()