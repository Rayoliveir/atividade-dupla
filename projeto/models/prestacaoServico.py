from models.abstracts.juridica import PessoaJuridica


class PrestacaoServico:
    def __init__(self, contratoInicio: str, contratoFim: str, dadosJuridico: PessoaJuridica) -> None:
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim
        self.dadosJuridico = dadosJuridico

    def __str__(self) -> str:
            return(
                f"{self.dadosJuridico}"
                f"\nInicio do contrato: {self.contratoInicio}"
                f"\nFim doontrato: {self.contratoFim}"
                    )
