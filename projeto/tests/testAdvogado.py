from models.abstracts.fisica import PessoaFisica
from models.abstracts.funcionario import Funcionario
from models.abstracts.pessoa import DadosPessoa
from models.advogado import Advogado
from models.endereco import Endereco
from models.enums.estadoCivil import EstadoCivil
from models.enums.genero import Genero
from models.enums.setor import Setor
from models.enums.unidadeFederativa import UnidadeFederativa

def validar_advogado():
    return Advogado("oab", 
            Funcionario("123.456.789-00", "12.345.678-00", "1111", Setor.JURIDICO, 5000.00, 
            PessoaFisica(Genero.MASCULINO, EstadoCivil.DIVORCIADO, "DD/MM/AAAA", 
            DadosPessoa(333, "Gustao Lima", "7199999-9999", "caio@gmail.com", 
            Endereco("Rua D. Pedro II", "57", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA)))))

#validando atributos

def test_id_valido(advogado_valido):
    assert advogado_valido.id == 18

def test_nome_valido(advogado_valido):
    assert advogado_valido.nome == "José Tigrão"

def test_telefone_valido(advogado_valido):
    assert advogado_valido.telefone == "9899-9999"

def test_email_valido(advogado_valido):
    assert advogado_valido.email == "bondedotigrao@gmail.com"

def test_logradouro_valido(advogado_valido):
    assert advogado_valido.endereco.logradouro == "alameda"

def test_numero_valido(advogado_valido):
    assert advogado_valido.endereco.numero == "123"

def test_complemento_valido(advogado_valido):
    assert advogado_valido.endereco.complemento == "ali na esquina"

def test_cep_valido(advogado_valido):
    assert advogado_valido.endereco.cep == "40.000-000"

def test_cidade_valido(advogado_valido):
    assert advogado_valido.endereco.cidade == "salvador"

def test_uf_valido(advogado_valido):
    assert advogado_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(advogado_valido):
    assert advogado_valido.sexo == Genero.MASCULINO

def test_estado_civil_valido(advogado_valido):
    assert advogado_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(advogado_valido):
    assert advogado_valido.dataNascimento == "24/09/1999"

def test_cpf_valido(advogado_valido):
    assert advogado_valido.cpf == "825.863.350-31"

def test_rg_valido(advogado_valido):
    assert advogado_valido.rg == "27.795.968-8"

def test_matricula_valido(advogado_valido):
    assert advogado_valido.matricula == "007"

def test_setor_valido(advogado_valido):
    assert advogado_valido.setor == Setor.JURIDICO

def test_salario_valido(advogado_valido):
    assert advogado_valido.salario == 7000.0

def test_oab_valido(advogado_valido):
    assert advogado_valido.oab == "32575756"