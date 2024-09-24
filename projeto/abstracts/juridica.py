import os
os.system("cls || clear")

class Juridica:
    def __init__(self, cnpj: str, incricaoEstadual: str) -> None:
        self.cnpj = cnpj
        self.inscricaoEstadual = incricaoEstadual

    def __str__(self) -> str:
        return(
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
        )
        