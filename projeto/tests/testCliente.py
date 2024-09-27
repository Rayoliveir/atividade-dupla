from models.abstracts.fisica import PessoaFisica
from models.abstracts.pessoa import DadosPessoa
from models.cliente import Cliente
from models.endereco import Endereco
from models.enums.estadoCivil import EstadoCivil
from models.enums.genero import Genero
from models.enums.unidadeFederativa import UnidadeFederativa

def validar_cliente():
    return Cliente("protocolo", 
            PessoaFisica(Genero.FEMININO, EstadoCivil.SOLTEIRO, "DD/MM/AAAA",
            DadosPessoa(333, "Gabriela Pitaya", "7199999-9999", "gabriela@gmail.com", 
            Endereco("Rua D. Pedro II", "43", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA))))