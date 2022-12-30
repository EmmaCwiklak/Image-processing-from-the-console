def pathInput():
    path = input('Podaj sciezke do zjecia: ')
    return path

def selectingEdiction():
    choice = int(input("Co zrobic? : \n[1]-wyszarzac\n[2]-obrocic\n[3]\n"))

    match choice:
        case 1:
            return print("Wyszarzanie")
        case _:
            return print("Nic nie podales")
