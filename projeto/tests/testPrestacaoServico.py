from projeto.models.abstracts.juridica import PessoaJuridica
from projeto.models.abstracts.pessoa import DadosPessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UnidadeFederativa
from projeto.models.prestacaoServico import PrestacaoServico


def validar_prestacao_servico():
    return PrestacaoServico("Contrato inicio", "Contrato fim", 
            PessoaJuridica("cnpj", "Inscricao estadual", 
            DadosPessoa(333, "Marta Magal", "7199999-9999", "Marta@gmail.com", 
            Endereco("Rua D. Pedro II", "28", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA))))