from abc import ABC, abstractmethod

from projeto.models.pessoa import DadosPessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.genero import Genero

class PessoaFisica(DadosPessoa, ABC):
    @abstractmethod
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: 
        Genero, estadoCivil: EstadoCivil, dataNascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento
        
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nSexo: {self.sexo}"
            f"\nEstado civil: {self.estadoCivil}"
            f"\nData de nascimento: {self.dataNascimento}"
        )
