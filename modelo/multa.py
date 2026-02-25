class Multa:
    def __init__(self, id_multa, placa, conductor, valor, tipo, estado="Pendiente"):
        self._id = id_multa
        self._placa = placa
        self._conductor = conductor
        self._valor = valor
        self._tipo = tipo
        self._estado = estado

    # GETTERS
    def get_id(self):
        return self._id

    def get_placa(self):
        return self._placa

    def get_conductor(self):
        return self._conductor

    def get_valor(self):
        return self._valor

    def get_tipo(self):
        return self._tipo

    def get_estado(self):
        return self._estado

    # SETTERS
    def set_valor(self, valor):
        self._valor = valor

    def set_estado(self, estado):
        self._estado = estado

    def to_dict(self):
        return {
            "id": self._id,
            "placa": self._placa,
            "conductor": self._conductor,
            "valor": self._valor,
            "tipo": self._tipo,
            "estado": self._estado
        }

    @staticmethod
    def from_dict(data):
        return Multa(
            data["id"],
            data["placa"],
            data["conductor"],
            data["valor"],
            data["tipo"],
            data["estado"]
        )

    def __str__(self):
        return f"ID:{self._id} | Placa:{self._placa} | Conductor:{self._conductor} | ${self._valor} | {self._tipo} | {self._estado}"