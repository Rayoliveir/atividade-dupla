from models.abstracts.juridica import PessoaJuridica


class Fornecedor:
    def __init__(self, nomeProduto: str, dadosJuridico: PessoaJuridica) -> None:
        self.produto = nomeProduto
        self.dadosJuridicos = dadosJuridico

    def __str__(self) -> str:
        return (
            f"{self.dadosJuridicos}"
            f"\nNome do produto: {self.produto}"
        )
