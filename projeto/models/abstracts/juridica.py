from abc import ABC

from models.abstracts.pessoa import DadosPessoa

class PessoaJuridica(ABC):
    def __init__(self, cnpj: str, inscricaoEstadual: str, dadosPessoa: DadosPessoa) -> None:
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual
        self.dadosPessoa = dadosPessoa

    def __str__(self) -> str:
        return (
            f"{self.dadosPessoa}"
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
        )
