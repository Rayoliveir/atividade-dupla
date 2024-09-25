from projeto.models.abstracts.fisica import PessoaFisica
from projeto.models.abstracts.funcionario import Funcionario
from projeto.models.abstracts.pessoa import DadosPessoa
from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.setor import Setor
from projeto.models.enums.unidadeFederativa import UnidadeFederativa

def validar_engenheiro():
    return Engenheiro("crea", 
            Funcionario("123.456.789-00", "12.345.678-00", "2222", Setor.ENGENHARIA, 4000.00, 
            PessoaFisica(Genero.MASCULINO, EstadoCivil.VIUVO, "DD/MM/AAAA",
            DadosPessoa(333, "Bruno Fernandes", "7199999-9999", "Bruno@gmail.com", 
            Endereco("Rua D. Pedro II", "23", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA)))))