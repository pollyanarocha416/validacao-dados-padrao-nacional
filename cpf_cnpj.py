from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos esta incorreta!!!")


class DocCpf:
    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido")
    
    def __str__(self) -> str:
        return self.formart_cpf()
    
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def formart_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido")

    def __str__(self) -> str:
        return self.formart_cnpj()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formart_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
