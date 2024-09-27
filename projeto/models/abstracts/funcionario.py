from abc import ABC

from models.abstracts.fisica import PessoaFisica
from models.enums.setor import Setor
from models.abstracts.pessoa import DadosPessoa
from models.enums.estadoCivil import EstadoCivil
from models.enums.genero import Genero

class Funcionario(PessoaFisica ,ABC):
    def __init__(self, sexo: Genero, estadoCivil: EstadoCivil, dataNascimento: str, dadosPessoa: 
                 DadosPessoa, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(sexo, estadoCivil, dataNascimento, dadosPessoa)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\n*== DADOS DO FUNCIONARIO ==*"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatricula: {self.matricula}"
            f"\nSetor: {self.setor}"
            f"\nSalario: {self.salario}"
        )
