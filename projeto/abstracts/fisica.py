from projeto.models.enums.genero import Genero
from projeto.models.enums.estadoCivil import EstadoCivil

import os
os.system("cls || clear")

class Fisica:
    def __init__(self, genero: Genero, estadoCivil: EstadoCivil, nascimento: str) -> None:
        self.genero = Genero
        self.estadoCivil = EstadoCivil
        self.nascimento = nascimento

    def __str__(self) -> str:
        return(
            f"\nGênero: {self.genero}"
            f"\nEstado civil: {self.estadoCivil}"
            f"\nData de nascimento: {self.nascimento}"
        )
        