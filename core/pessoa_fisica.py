from core.cliente import Cliente


class PessoaFisica(Cliente):
    """Cliente do tipo pessoa física, identificado por CPF.

    Attributes:
        _cpf: CPF do cliente.
        _nome: Nome completo do cliente.
        _data_nascimento: Data de nascimento do cliente.
    """

    def __init__(self, endereco, cpf, nome, data_nascimento):
        """Inicializa um cliente pessoa física.

        Args:
            endereco: Endereço residencial do cliente.
            cpf: CPF do cliente.
            nome: Nome completo do cliente.
            data_nascimento: Data de nascimento do cliente.
        """
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        """str: CPF do cliente."""
        return self._cpf

    @property
    def nome(self):
        """str: Nome completo do cliente."""
        return self._nome

    @property
    def data_nascimento(self):
        """str: Data de nascimento do cliente."""
        return self._data_nascimento
    
