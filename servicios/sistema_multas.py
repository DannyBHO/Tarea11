import json
import os
from modelo.multa import Multa


class SistemaMultas:
    def __init__(self, archivo="multas.json"):
        self.archivo = archivo
        self.multas = {}  # diccionario
        self.cargar()

    def agregar_multa(self, multa):
        if multa.get_id() in self.multas:
            print(" Ya existe.")
        else:
            self.multas[multa.get_id()] = multa
            print(" Multa registrada.")
            self.guardar()

    def eliminar_multa(self, id_multa):
        if id_multa in self.multas:
            del self.multas[id_multa]
            print(" Eliminada.")
            self.guardar()
        else:
            print(" No encontrada.")

    def pagar_multa(self, id_multa):
        if id_multa in self.multas:
            self.multas[id_multa].set_estado("Pagado")
            print("💰 Multa pagada.")
            self.guardar()
        else:
            print(" No encontrada.")

    def buscar_por_placa(self, placa):
        resultados = [
            m for m in self.multas.values()
            if placa.lower() in m.get_placa().lower()
        ]

        for m in resultados:
            print(m)

    def mostrar_todas(self):
        if not self.multas:
            print("📭 Sin multas.")
        else:
            for m in self.multas.values():
                print(m)

    # ARCHIVOS
    def guardar(self):
        data = [m.to_dict() for m in self.multas.values()]
        with open(self.archivo, "w") as f:
            json.dump(data, f, indent=4)

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                try:
                    data = json.load(f)
                    for item in data:
                        multa = Multa.from_dict(item)
                        self.multas[multa.get_id()] = multa
                except:
                    self.multas = {}