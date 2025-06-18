import time

agenda = {} # Para guardar de dos en dos nombre y núm. de tfno,
            # clave = nombre, valor = num de tfno

def mostrar_contactos():
    print("\nName".ljust(20) + "Contact number")
    print("*" * 35)
    for nombre, numero in agenda.items():
        print(f"{nombre.ljust(20)}{numero}")


while True:
    print("\nCONTACT BOOK")
    print("1. Add new contact")
    print("2. Find contact")
    print("3. Show all contacts")
    print("4. Delete contact by name")
    print("5. Exit")

    opcion = int(input("Please introduce the number of the action you want to choose: "))

    match opcion:
        case 1:
            nombre = input("Name: ")
            numero = input("Phone number: ")

            agenda[nombre] = numero
            print(f"Contact {nombre} has been added correctly!")

        case 2:
            nombre_buscar = input("Introduce the name of the contact you want to find: ")
            if nombre_buscar in agenda:
                print(f"{nombre_buscar}'s number is: {agenda[nombre_buscar]}")
            else:
                print("Could not find name in contact book")

        case 3:
            if not agenda: # If the dictionary is empty
                print("\nYour contact book is empty.")
            else:
                mostrar_contactos()

        case 4:
            nombre_eliminar = input("Please, introduce the name of the contact you want to delete: ")

            if nombre_eliminar in agenda:
                agenda.pop(nombre_eliminar)
                print(f"{nombre_eliminar} has been deleted from your contact book.")
            else:
                print("Could not find name in contact book")

        case 5:
            print("Goodbye!")
            break

        case _:
            print("Invalid option")
            time.sleep(1)
