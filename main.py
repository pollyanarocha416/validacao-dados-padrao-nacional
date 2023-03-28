from cpf_cnpj import Documento
from telefonebr import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco


exemplo_cpf = "70373061269"
exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
#print(documento)


telefone = "556992451580"
tel_objto = TelefonesBr(telefone)
#print(tel_objto)


cadastro = DatasBr()
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)


hoje = DatasBr()
print(hoje.tempo_cadastro())


cep = "01153000"
objt_cep = BuscaEndereco(cep)
print(objt_cep)
bairro, cidade, uf = objt_cep.acessa_via_cep()
print(bairro, cidade, uf)
