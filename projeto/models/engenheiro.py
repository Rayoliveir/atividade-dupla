from models.abstracts.funcionario import Funcionario


class Engenheiro:
    def __init__(self, crea: str, dadosFuncionario: Funcionario) -> None:
        self.crea = crea
        self.dadosFuncionario = dadosFuncionario

    def __str__(self) -> str:
        return (
            f"{self.dadosFuncionario}"
            f"\nCREA: {self.crea}"
        )