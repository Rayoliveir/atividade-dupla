import pytest


from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.unidadeFederativa import UnidadeFederativa
from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco


@pytest.fixture
def cliente_valido():
    return Cliente(18, "Nome", "Telefone", "Email",
                    Endereco("Lomgradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,"24/09/1999",7777)

#validando atributos
def test_atributo_nome_valido(cliente_valido):
    assert cliente_valido.nome == "Nome"

def test_atributo_id_valido(cliente_valido):
    assert cliente_valido.id == 18

def test_atributo_telefone_valido(cliente_valido):
    assert cliente_valido.telefone == "Telefone"

def test_atributo_email_valido(cliente_valido):
    assert cliente_valido.email == "Email"

def test_logradouro_valido(cliente_valido):
    assert cliente_valido.endereco.logradouro == "Lomgradouro"

def test_numero_valido(cliente_valido):
    assert cliente_valido.endereco.numero == "Numero"

def test_complemento_valido(cliente_valido):
    assert cliente_valido.endereco.complemento == "Complemento"

def test_cep_valido(cliente_valido):
    assert cliente_valido.endereco.cep == "cep"

def test_cidade_valido(cliente_valido):
    assert cliente_valido.endereco.cidade == "Cidade"

def test_uf_valido(cliente_valido):
    assert cliente_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(cliente_valido):
    assert cliente_valido.sexo == Genero.MASCULINO

def test_estado_civil_valido(cliente_valido):
    assert cliente_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(cliente_valido):
    assert cliente_valido.dataNascimento == "24/09/1999"

def test_protocolo_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloAtendimento == 7777


#testando exceções
def test_id_tipo_errado(cliente_valido):
    with pytest.raises(TypeError, match = "valor inválido"):
        Cliente("f", "Nome", "Telefone", "Email",
                    Endereco("Lomgradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999",7777)

def test_id_valor_negativo(cliente_valido):
    with pytest.raises(ValueError, match = "valor inválido"):
        Cliente(-18, "Nome", "Telefone", "Email",
                    Endereco("Lomgradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999",7777)

def test_nome_vazio(cliente_valido):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Cliente(18, "", "Telefone", "Email",
                    Endereco("Lomgradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999",7777)

def test_cep_invalido(cliente_valido):
    with pytest.raises(match = "CEP inválido"):
        Cliente(18, "Nome", "Telefone", "Email",
                    Endereco("Lomgradouro", "Numero", "Complemento", "cep0", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", 7777)
