from __future__ import annotations
import random

class Conta:
    """Representa uma conta bancária vinculada a um cliente.

    Attributes:
        _saldo: Saldo atual da conta.
        _numero: Número único da conta gerado aleatoriamente.
        _agencia: Número da agência (fixo em "0001").
        _cliente: Cliente titular da conta.
        _historico: Histórico de transações da conta.
    """

    def __init__(self, cliente: Cliente, historico: Historico):
        """Inicializa a conta com número aleatório, agência padrão e saldo zero.

        Args:
            cliente: Cliente titular da conta.
            historico: Histórico de transações da conta.
        """
        self._saldo = 0
        self._numero = random.randint(10000, 99999)
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self) -> float:
        """float: Saldo atual da conta."""
        return self._saldo

    @property
    def numero(self) -> int:
        """int: Número único da conta."""
        return self._numero

    @property
    def agencia(self) -> str:
        """str: Número da agência."""
        return self._agencia

    @property
    def cliente(self) -> Cliente:
        """Cliente: Titular da conta."""
        return self._cliente

    @property
    def historico(self) -> Historico:
        """Historico: Histórico de transações da conta."""
        return self._historico

    @classmethod
    def nova_conta(cls, cliente: Cliente, historico: Historico):
        """Cria uma nova Conta.

        Args:
            cliente: Cliente titular da conta.
            historico: Histórico de transações da conta.

        Returns:
            Conta: Nova instância de Conta.
        """
        return cls(cliente, historico)

    def sacar(self, valor: float) -> bool:
        """Realiza um saque na conta se houver saldo suficiente.

        Args:
            valor: Valor a ser sacado.

        Returns:
            True se o saque foi realizado, False se saldo insuficiente.
        """
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def depositar(self, valor: float) -> bool:
        """Realiza um depósito na conta se o valor for positivo.

        Args:
            valor: Valor a ser depositado.

        Returns:
            True se o depósito foi realizado, False se o valor for inválido.
        """
        if valor > 0:
            self._saldo += valor
            return True
        return False