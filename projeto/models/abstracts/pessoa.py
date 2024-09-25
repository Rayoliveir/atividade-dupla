from abc import ABC

from models.endereco import Endereco


class DadosPessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str,  email: str, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"\n*== DADOS PESSOA ==*"
            f"\nD: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\n\n-- ENDEREÇO --: {self.endereco}"
        )
