import pytest

from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor
from projeto.models.enums.unidadeFederativa import UnidadeFederativa


@pytest.fixture

def validar_advogado():
    return Advogado(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "Cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0,"32575756")

#validando atributos

def test_id_valido(validar_advogado):
    assert validar_advogado.id == 18

def test_nome_valido(validar_advogado):
    assert validar_advogado.nome == "Nome"

def test_telefone_valido(validar_advogado):
    assert validar_advogado.telefone == "Telefone"

def test_email_valido(validar_advogado):
    assert validar_advogado.email == "Email"

def test_logradouro_valido(validar_advogado):
    assert validar_advogado.endereco.logradouro == "Longradouro"

def test_numero_valido(validar_advogado):
    assert validar_advogado.endereco.numero == "Numero"

def test_complemento_valido(validar_advogado):
    assert validar_advogado.endereco.complemento == "Complemento"

def test_cep_valido(validar_advogado):
    assert validar_advogado.endereco.cep == "cep"

def test_cidade_valido(validar_advogado):
    assert validar_advogado.endereco.cidade == "Cidade"

def test_uf_valido(validar_advogado):
    assert validar_advogado.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(validar_advogado):
    assert validar_advogado.sexo == Genero.MASCULINO

def test_estado_civil_valido(validar_advogado):
    assert validar_advogado.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(validar_advogado):
    assert validar_advogado.dataNascimento == "DD/MM/AAAA"

def test_cpf_valido(validar_advogado):
    assert validar_advogado.cpf == "Cpf"

def test_rg_valido(validar_advogado):
    assert validar_advogado.rg == "rg"

def test_matricula_valido(validar_advogado):
    assert validar_advogado.matricula == "Matricula"

def test_setor_valido(validar_advogado):
    assert validar_advogado.setor == Setor.JURIDICO

def test_salario_valido(validar_advogado):
    assert validar_advogado.salario == 7000.0

def test_oab_valido(validar_advogado):
    assert validar_advogado.oab == "32575756"

#testando exceções
def test_id_tipo_errado(validar_advogado):
    with pytest.raises(TypeError, match = "valor inválido"):
        Advogado("f", "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "Cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0,"32575756")

def test_id_valor_negativo(validar_advogado):
    with pytest.raises(ValueError, match = "valor inválido"):
        Advogado(-18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "Cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0,"32575756")

def test_nome_vazio(validar_advogado):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Advogado(18, "", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "Cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0,"32575756")

def test_salario_tipo_errado(validar_advogado):
    with pytest.raises(TypeError, match = "dado incorreto"):
        Advogado(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "Cpf", "rg", "Matricula", Setor.JURIDICO, "7000.0","32575756")

def test_salario_negativo(validar_advogado):
    with pytest.raises(ValueError, match = "salário não pode ser negativo"):
        Advogado(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "Cpf", "rg", "Matricula", Setor.JURIDICO, -7000.0,"32575756")

def test_cep_invalido(validar_advogado):
    with pytest.raises(match = "CEP inválido"):
        Advogado(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep0", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "Cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0,"32575756")
        
def test_rg_invalido(validar_advogado):
    with pytest.raises( match = "RG inválido"):
        Advogado(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "Cpf", "rg0", "Matricula", Setor.JURIDICO, 7000.0,"32575756")

def test_cpf_invalido(validar_advogado):
    with pytest.raises( match = "CPF inválido"):
        Advogado(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "Cpf0", "rg", "Matricula", Setor.JURIDICO, 7000.0,"32575756")