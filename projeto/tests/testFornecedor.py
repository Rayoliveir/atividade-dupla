from models.abstracts.juridica import PessoaJuridica
from models.abstracts.pessoa import DadosPessoa
from models.endereco import Endereco
from models.enums.unidadeFederativa import UnidadeFederativa
from models.fornecedor import Fornecedor


def validar_fornecedor():
    return Fornecedor("Nome produto", 
            PessoaJuridica("cnpj", "Inscricao estadual", 
            DadosPessoa(333, "Jackson Oliveira", "7199999-9999", "jackson@gmail.com", 
            Endereco("Rua D. Pedro II", "62", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA))))



