import random

from models.abstracts.fisica import PessoaFisica


class Cliente:
    # def geradorNumeroProtocolo(self):
    #     min_value = 10**16
    #     max_value = 10**17 - 1
    #     random_protocolo = random.randint(min_value, max_value)
    #     return random_protocolo


    def __init__(self, protocoloAtendimento: str, dadosCliente: PessoaFisica) -> None:
        self.protocoloAtendimento = protocoloAtendimento
        self.dadosCliente = dadosCliente

    def __str__(self) -> str:
        return (
            f"{self.dadosCliente}"
            f"\nNúmero de protocolo: {self.protocoloAtendimento}"
        )