from __future__ import annotations
from core.conta import Conta
from core.cliente import Cliente


class ContaCorrente(Conta):
    """Conta corrente com limite de crédito e limite de saques diários.

    Attributes:
        _limite: Valor máximo permitido para saque além do saldo.
        _saques: Número máximo de saques permitidos por período.
    """

    def __init__(self, cliente, historico=None, limite=500.0, saques=3):
        """Inicializa uma ContaCorrente.

        Args:
            cliente: Cliente titular da conta.
            historico: Histórico de transações. Se None, um novo é criado pela classe pai.
            limite: Limite de crédito disponível para saque. Padrão: 500.0.
            saques: Número máximo de saques permitidos. Padrão: 3.
        """
        super().__init__(cliente, historico)
        self._limite = limite
        self._saques = saques

    @property
    def limite(self):
        """float: Limite de crédito disponível para saque."""
        return self._limite

    @property
    def saques(self):
        """int: Número máximo de saques permitidos."""
        return self._saques

    @classmethod
    def nova_conta(cls, cliente: Cliente, historico: Historico, limite: float = 500.0, saques: int = 3):
        """Cria uma nova ContaCorrente.

        Args:
            cliente: Cliente titular da conta.
            historico: Histórico de transações da conta.
            limite: Limite de crédito disponível para saque. Padrão: 500.0.
            saques: Número máximo de saques permitidos. Padrão: 3.

        Returns:
            ContaCorrente: Nova instância de ContaCorrente.
        """
        return cls(cliente, historico, limite, saques)
    
