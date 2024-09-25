from abc import ABC

from models.abstracts.pessoa import DadosPessoa
from models.enums.estadoCivil import EstadoCivil
from models.enums.genero import Genero

class PessoaFisica(ABC):
    def __init__(self, sexo: Genero, estadoCivil: EstadoCivil, dataNascimento: str, dadosPessoa: DadosPessoa) -> None:
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento
        self.dadosPessoa = dadosPessoa


    def __str__(self) -> str:
        return (
            f"{self.dadosPessoa}"
            f"\nSexo: {self.sexo}"
            f"\nEstado civil: {self.estadoCivil}"
            f"\nData de nascimento: {self.dataNascimento}"
        )