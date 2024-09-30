from projeto.models.abstracts.funcionario import Funcionario
from projeto.models.abstracts.pessoa import DadosPessoa
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor


class Engenheiro(Funcionario):
    def __init__(self, crea: str, sexo: Genero, estadoCivil: 
        EstadoCivil, dataNascimento: str, dadosPessoa: DadosPessoa, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(sexo, estadoCivil, dataNascimento, dadosPessoa, cpf, rg, matricula, setor, salario)
        self.crea = crea

  
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCREA: {self.crea}"
            )
  
  
    # def __init__(self, crea: str, dadosFuncionario: Funcionario) -> None:
    #     self.dadosFuncionario = dadosFuncionario

    # def __str__(self) -> str:
    #     return (
    #         f"{self.dadosFuncionario}"
    #     )