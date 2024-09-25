import os

# Importaçoes
from models.abstracts.fisica import PessoaFisica
from models.abstracts.funcionario import Funcionario
from models.abstracts.pessoa import DadosPessoa
from models.advogado import Advogado
from models.endereco import Endereco
from models.enums.estadoCivil import EstadoCivil
from models.enums.genero import Genero
from models.enums.setor import Setor
from models.enums.unidadeFederativa import UnidadeFederativa
from models.abstracts.juridica import PessoaJuridica
from models.cliente import Cliente
from models.engenheiro import Engenheiro
from models.fornecedor import Fornecedor
from models.medico import Medico
from models.prestacaoServico import PrestacaoServico


os.system("cls || clear")

advogado = Advogado("oab", 
            Funcionario("123.456.789-00", "12.345.678-00", "1111", Setor.JURIDICO, 5000.00, 
            PessoaFisica(Genero.MASCULINO, EstadoCivil.DIVORCIADO, "DD/MM/AAAA", 
            DadosPessoa(333, "Gustao Lima", "7199999-9999", "caio@gmail.com", 
            Endereco("Rua D. Pedro II", "57", "Centro", "47.400-000", "Xique-xique", 
            UnidadeFederativa.BAHIA)))))

engenheiro = Engenheiro("crea", 
                Funcionario("123.456.789-00", "12.345.678-00", "2222", Setor.ENGENHARIA, 4000.00, 
                PessoaFisica(Genero.MASCULINO, EstadoCivil.VIUVO, "DD/MM/AAAA",
                DadosPessoa(333, "Bruno Fernandes", "7199999-9999", "Bruno@gmail.com", 
                Endereco("Rua D. Pedro II", "23", "Centro", "47.400-000", "Xique-xique", 
                UnidadeFederativa.BAHIA)))))

medico = Medico("crm", Funcionario("123.456.789-00", "12.345.678-00", "3333", Setor.SAUDE, 3000.00, 
                PessoaFisica(Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA",
                DadosPessoa(333, "Josue Reis", "7199999-9999", "josue@gmail.com", 
                Endereco("Rua D. Pedro II", "98", "Centro", "47.400-000", "Xique-xique", 
                UnidadeFederativa.BAHIA)))))

cliente = Cliente("protocolo", 
                PessoaFisica(Genero.FEMININO, EstadoCivil.SOLTEIRO, "DD/MM/AAAA",
                DadosPessoa(333, "Gabriela Pitaya", "7199999-9999", "gabriela@gmail.com", 
                Endereco("Rua D. Pedro II", "43", "Centro", "47.400-000", "Xique-xique", 
                UnidadeFederativa.BAHIA))))

fornecedor = Fornecedor("Nome produto", 
                PessoaJuridica("cnpj", "Inscricao estadual", 
                DadosPessoa(333, "Jackson Oliveira", "7199999-9999", "jackson@gmail.com", 
                Endereco("Rua D. Pedro II", "62", "Centro", "47.400-000", "Xique-xique", 
                UnidadeFederativa.BAHIA))))


prestacaoServico = PrestacaoServico("Contrato inicio", "Contrato fim", 
                    PessoaJuridica("cnpj", "Inscricao estadual", 
                    DadosPessoa(333, "Marta Magal", "7199999-9999", "Marta@gmail.com", 
                    Endereco("Rua D. Pedro II", "28", "Centro", "47.400-000", "Xique-xique", 
                    UnidadeFederativa.BAHIA))))

print("======== Advogado ========")
print(advogado)
print()
print("======== Engenheiro ========")
print(engenheiro)
print()
print("======== Médico ========")
print(medico)
print()
print("======== Cliente ========")
print(cliente)
print()
print("======== Fornecedor ========")
print(fornecedor)
print()
print("======== Prestação de serviço ========")
print(prestacaoServico)