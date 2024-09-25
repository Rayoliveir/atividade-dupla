from projeto.models.abstracts.fisica import PessoaFisica
from projeto.models.abstracts.pessoa import DadosPessoa
from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.genero import Genero
from projeto.models.enums.unidadeFederativa import UnidadeFederativa

def validar_cliente():
    return Cliente("protocolo", 
            PessoaFisica(Genero.FEMININO, EstadoCivil.SOLTEIRO, "DD/MM/AAAA",
            DadosPessoa(333, "Gabriela Pitaya", "7199999-9999", "gabriela@gmail.com", 
            Endereco("Rua D. Pedro II", "43", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA))))