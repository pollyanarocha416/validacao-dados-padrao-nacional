from cpf_cnpj import Documento
from telefonebr import TelefonesBr

exemplo_cpf = "70373061269"
exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

telefone = "556992451580"
tel_objto = TelefonesBr(telefone)
print(tel_objto)