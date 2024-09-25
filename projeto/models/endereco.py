from models.enums.unidadeFederativa import UnidadeFederativa


class Endereco:
    def __init__(self, longradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.longradouro = longradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return (
            f"\nLongradouro: {self.longradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCidade: {self.cidade}"
            f"\nCEP: {self.cep}"
            f"\nUnidade Federativa: {self.uf}"
        )