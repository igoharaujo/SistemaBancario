from __future__ import annotations

class Cliente:
    """Representa um cliente do banco.

    Attributes:
        _endereco: Endereço residencial do cliente.
        _contas: Lista de contas associadas ao cliente.
    """

    def __init__(self, endereco: str):
        """Inicializa um Cliente com endereço e lista de contas vazia.

        Args:
            endereco: Endereço residencial do cliente.
        """
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        """str: Endereço residencial do cliente."""
        return self._endereco

    @property
    def contas(self):
        """list: Lista de contas associadas ao cliente."""
        return self._contas

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        """Realiza uma transação em uma conta do cliente.

        Args:
            conta: Conta na qual a transação será registrada.
            transacao: Transação a ser executada.
        """
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        """Adiciona uma conta à lista de contas do cliente.

        Args:
            conta: Conta a ser adicionada.
        """
        self._contas.append(conta)


    