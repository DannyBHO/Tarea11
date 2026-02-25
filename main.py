from servicios.sistema_multas import SistemaMultas
from modelo.multa import Multa


def menu():
    print("\n===== SISTEMA DE MULTAS =====")
    print("1. Registrar multa")
    print("2. Eliminar multa")
    print("3. Pagar multa")
    print("4. Buscar por placa")
    print("5. Mostrar todas")
    print("6. Salir")


def main():
    sistema = SistemaMultas()

    while True:
        menu()
        op = input("Opción: ")

        if op == "1":
            id_m = input("ID: ")
            placa = input("Placa: ")
            conductor = input("Conductor: ")
            valor = float(input("Valor: "))
            tipo = input("Tipo de infracción: ")

            multa = Multa(id_m, placa, conductor, valor, tipo)
            sistema.agregar_multa(multa)

        elif op == "2":
            sistema.eliminar_multa(input("ID: "))

        elif op == "3":
            sistema.pagar_multa(input("ID: "))

        elif op == "4":
            sistema.buscar_por_placa(input("Placa: "))

        elif op == "5":
            sistema.mostrar_todas()

        elif op == "6":
            break
        
        else:
            print(" Opción inválida")


if __name__ == "__main__":
    main()