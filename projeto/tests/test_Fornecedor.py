import pytest

from projeto.models.endereco import Endereco
from projeto.models.fornecedor import Fornecedor
from projeto.models.enums.unidadeFederativa import UnidadeFederativa




@pytest.fixture
def fornecedor_valido():
        return Fornecedor(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Nuemro", "Complemento", "Cep", "Cidade", UnidadeFederativa.BAHIA),
                    "cnpj","5277216-46","Hardware")

#validando atributos
def test_id_valido(fornecedor_valido):
    assert fornecedor_valido.id == 18

def test_nome_valido(fornecedor_valido):
    assert fornecedor_valido.nome == "Nome"

def test_telefone_valido(fornecedor_valido):
    assert fornecedor_valido.telefone == "Telefone"

def test_email_valido(fornecedor_valido):
    assert fornecedor_valido.email == "Email"

def test_logradouro_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.logradouro == "Longradouro"

def test_numero_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.numero == "Nuemro"

def test_complemento_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.complemento == "Complemento"

def test_cep_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cep == "40.000-000"

def test_cidade_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cidade == "salvador"

def test_uf_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_cnpj_valido(fornecedor_valido):
    assert fornecedor_valido.cnpj == "cnpj"

def test_inscricao_estadual_valida(fornecedor_valido):
    assert fornecedor_valido.inscricaoEstadual == "5277216-46"

def test_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Hardware"

#testando exceções
def test_id_tipo_errado(fornecedor_valido):
    with pytest.raises(TypeError, match = "valor inválido"):
        Fornecedor("f", "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Nuemro", "Complemento", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "cnpj","5277216-46","Hardware")

def test_id_valor_negativo(fornecedor_valido):
    with pytest.raises(ValueError, match = "valor inválido"):
        Fornecedor(-18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Nuemro", "Complemento", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "cnpj","5277216-46","Hardware")

def test_nome_vazio(fornecedor_valido):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Fornecedor(18, "", "Telefone", "Email",
                    Endereco("Longradouro", "Nuemro", "Complemento", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "cnpj","5277216-46","Hardware")

def test_cep_invalido(fornecedor_valido):
    with pytest.raises(match = "CEP inválido"):
        Fornecedor(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Nuemro", "Complemento", "40.000-0000", "salvador", UnidadeFederativa.BAHIA),
                    "cnpj","5277216-46","Hardware")