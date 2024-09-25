from models.abstracts.funcionario import Funcionario


class Medico:
    def __init__(self, crm: str, dadosFuncionario: Funcionario) -> None:
        self.crm = crm
        self.dadosFuncionario = dadosFuncionario

    def __str__(self) -> str:
        return (
            f"{self.dadosFuncionario}"
            f"\nCRM: {self.crm}"
        )