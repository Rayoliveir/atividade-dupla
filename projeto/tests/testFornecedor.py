from projeto.models.abstracts.juridica import PessoaJuridica
from projeto.models.abstracts.pessoa import DadosPessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UnidadeFederativa
from projeto.models.fornecedor import Fornecedor


def validar_fornecedor():
    return Fornecedor("Nome produto", 
            PessoaJuridica("cnpj", "Inscricao estadual", 
            DadosPessoa(333, "Jackson Oliveira", "7199999-9999", "jackson@gmail.com", 
            Endereco("Rua D. Pedro II", "62", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA))))

def test_fornecedor_atributo_NomeProduto(validar_fornecedor):
    assert validar_fornecedor.fornecedor.nomeProduto == "Nome produto"

