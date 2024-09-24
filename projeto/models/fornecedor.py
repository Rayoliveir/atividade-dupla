from projeto.abstracts.juridica import Juridica
import os
os.system("cls || clear")

class Fornecedor(Juridica):
    def __init__(self, cnpj: str, incricaoEstadual: str) -> None:
        super().__init__(cnpj, incricaoEstadual)

    def __str__(self) -> str:
        return (
                f"{super().__str__()}"
                f"Produto: {self.produto}"        