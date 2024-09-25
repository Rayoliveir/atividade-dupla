from projeto.models.abstracts.fisica import PessoaFisica
from projeto.models.abstracts.funcionario import Funcionario
from projeto.models.abstracts.pessoa import DadosPessoa
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor
from projeto.models.enums.unidadeFederativa import UnidadeFederativa

def validar_advogado():
    return Advogado("oab", 
            Funcionario("123.456.789-00", "12.345.678-00", "1111", Setor.JURIDICO, 5000.00, 
            PessoaFisica(Genero.MASCULINO, EstadoCivil.DIVORCIADO, "DD/MM/AAAA", 
            DadosPessoa(333, "Gustao Lima", "7199999-9999", "caio@gmail.com", 
            Endereco("Rua D. Pedro II", "57", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA)))))