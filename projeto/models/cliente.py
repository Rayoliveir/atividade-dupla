from projeto.models.funcionario import Funcionario
from projeto.models.pessoa import DadosPessoa
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor


class Cliente(Funcionario):
    def __init__(self, protocoloAtendimento: str, sexo: Genero, estadoCivil: 
        EstadoCivil, dataNascimento: str, dadosPessoa: DadosPessoa, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(sexo, estadoCivil, dataNascimento, dadosPessoa, cpf, rg, matricula, setor, salario)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nNúmero de protocolo: {self.protocoloAtendimento}"
            )
