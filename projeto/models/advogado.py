from models.abstracts.funcionario import Funcionario

class Advogado:
    def __init__(self, oab: str, dadosFuncionario: Funcionario) -> None:
        self.oab = oab
        self.dadosFuncionario = dadosFuncionario

    def __str__(self) -> str:
        return (
            f"{self.dadosFuncionario}"
            f"\nOAB: {self.oab}"
        )