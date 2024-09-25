from abc import ABC

from models.abstracts.fisica import PessoaFisica
from models.enums.setor import Setor

class Funcionario(ABC):
    def __init__(self, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, dadosPessoa: PessoaFisica) -> None:
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario
        self.dadosPessoa = dadosPessoa

    def __str__(self) -> str:
        return (
            f"{self.dadosPessoa}"
            f"\n\n*== DADOS DO FUNCIONARIO ==*"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatricula: {self.matricula}"
            f"\nSetor: {self.setor}"
            f"\nSalario: {self.salario}"
        )