from projeto.abstracts.juridica import Juridica
import os
os.system("cls || clear")

class PrestacaoServico:
    def __init__(self, contratoInicio: str, contratoFim: str) -> None:
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
            return(f"\nContrato inicial: {self.contratoInicio}"
                    f"\nContrato final: {self.contratoFim}")