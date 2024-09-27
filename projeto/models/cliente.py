import random

from models.abstracts.funcionario import Funcionario
from models.abstracts.pessoa import DadosPessoa
from models.enums.estadoCivil import EstadoCivil
from models.enums.genero import Genero
from models.enums.setor import Setor



class Cliente(Funcionario):
    def __init__(self, protocoloAtendimento: str, sexo: Genero, estadoCivil: EstadoCivil, dataNascimento: str, dadosPessoa: DadosPessoa, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(sexo, estadoCivil, dataNascimento, dadosPessoa, cpf, rg, matricula, setor, salario)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nNúmero de protocolo: {self.protocoloAtendimento}"
            )

    # def __init__(self, protocoloAtendimento: str, dadosCliente: PessoaFisica) -> None:
    #     self.dadosCliente = dadosCliente

    # def __str__(self) -> str:
    #     return (
    #         f"{self.dadosCliente}"
    #     )

    # def geradorNumeroProtocolo(self):
    #     min_value = 10**16
    #     max_value = 10**17 - 1
    #     random_protocolo = random.randint(min_value, max_value)
    #     return random_protocolo