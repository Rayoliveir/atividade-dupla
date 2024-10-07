import pytest


from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor
from projeto.models.enums.unidadeFederativa import UnidadeFederativa


@pytest.fixture
def engenheiro_valido():
    return Engenheiro(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA","cpf","rg","007",Setor.ENGENHARIA,7000.0,"99999")

#validando atributos

def test_id_valido(engenheiro_valido):
    assert engenheiro_valido.id == 18

def test_nome_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "Nome"

def test_telefone_valido(engenheiro_valido):
    assert engenheiro_valido.telefone == "Telefone"

def test_email_valido(engenheiro_valido):
    assert engenheiro_valido.email == "Email"

def test_logradouro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.logradouro == "Longradouro"

def test_numero_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.numero == "Numero"

def test_complemento_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.complemento == "Complemento"

def test_cep_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cep == "cep"

def test_cidade_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cidade == "Cidade"

def test_uf_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(engenheiro_valido):
    assert engenheiro_valido.sexo == Genero.MASCULINO

def test_estado_civil_valido(engenheiro_valido):
    assert engenheiro_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(engenheiro_valido):
    assert engenheiro_valido.dataNascimento == "DD/MM/AAAA"

def test_cpf_valido(engenheiro_valido):
    assert engenheiro_valido.cpf == "cpf"

def test_rg_valido(engenheiro_valido):
    assert engenheiro_valido.rg == "rg"

def test_matricula_valido(engenheiro_valido):
    assert engenheiro_valido.matricula == "007"

def test_setor_valido(engenheiro_valido):
    assert engenheiro_valido.setor == Setor.ENGENHARIA

def test_salario_valido(engenheiro_valido):
    assert engenheiro_valido.salario == 7000.0

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "99999"

#testando exceções
def test_id_tipo_errado(engenheiro_valido):
    with pytest.raises(TypeError, match = "valor inválido"):
        Engenheiro("f", "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "cpf", "rg", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_id_valor_negativo(engenheiro_valido):
    with pytest.raises(ValueError, match = "valor inválido"):
        Engenheiro(-18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "cpf", "rg", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_nome_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Engenheiro(18, "", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "cpf", "rg", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_salario_tipo_errado(engenheiro_valido):
    with pytest.raises(TypeError, match = "dado incorreto"):
        Engenheiro(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "cpf", "rg", "007", Setor.ENGENHARIA, "7000.0","32575756")

def test_salario_negativo(engenheiro_valido):
    with pytest.raises(ValueError, match = "salário não pode ser negativo"):
        Engenheiro(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "cpf", "rg", "007", Setor.ENGENHARIA, -7000.0,"32575756")

def test_cep_invalido(engenheiro_valido):
    with pytest.raises(match = "CEP inválido"):
        Engenheiro(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep0", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "cpf", "rg", "007", Setor.ENGENHARIA, 7000.0,"32575756")
        
def test_rg_invalido(engenheiro_valido):
    with pytest.raises(match = "RG inválido"):
        Engenheiro(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "cpf", "rg0", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_cpf_invalido(engenheiro_valido):
    with pytest.raises(match = "CPF inválido"):
        Engenheiro(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "cpf0", "rg", "007", Setor.ENGENHARIA, 7000.0,"32575756")