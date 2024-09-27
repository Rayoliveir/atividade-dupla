from models.abstracts.fisica import PessoaFisica
from models.abstracts.funcionario import Funcionario
from models.abstracts.pessoa import DadosPessoa
from models.endereco import Endereco
from models.enums.estadoCivil import EstadoCivil
from models.enums.genero import Genero
from models.enums.setor import Setor
from models.enums.unidadeFederativa import UnidadeFederativa
from models.medico import Medico


def validar_medico():
    return Medico("crm", 
            Funcionario("123.456.789-00", "12.345.678-00", "3333", Setor.SAUDE, 3000.00, 
            PessoaFisica(Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA",
            DadosPessoa(333, "Josue Reis", "7199999-9999", "josue@gmail.com", 
            Endereco("Rua D. Pedro II", "98", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA)))))