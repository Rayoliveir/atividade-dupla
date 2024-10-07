import os

from projeto.models.endereco import Endereco
# from models.classe.prestacaoServico import PrestacaoServico
from models.enums.unidadeFederativa import UnidadeFederativa
from projeto.models.medico import Medico
from models.enums.estadoCivil import EstadoCivil
from models.enums.genero import Genero
from models.enums.setor import Setor
from models.abstracts.pessoa import DadosPessoa

os.system("cls || clear")

# if __name__ == "__main__":
#     os.system("pytest")

medico = Medico("crm", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", 
                DadosPessoa(18, "Nome", "Telefone", "Email", 
                Endereco("Logradouro", 99, "Complemento", "CEP", "Cidade", UnidadeFederativa.BAHIA)))



print(medico)