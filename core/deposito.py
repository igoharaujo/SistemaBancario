from __future__ import annotations
from core.transacao import Transacao

class Depositar(Transacao):
    """Transação de depósito em uma conta bancária.

    Attributes:
        _valor: Valor a ser depositado.
    """

    def __init__(self, valor):
        """Inicializa a transação de depósito.

        Args:
            valor: Valor a ser depositado.
        """
        self._valor = valor

    @property
    def valor(self):
        """float: Valor a ser depositado."""
        return self._valor

    def registrar(self, conta: Conta):
        """Executa o depósito e registra a transação no histórico da conta.

        Args:
            conta: Conta na qual o depósito será realizado.
        """
        conta.depositar(self._valor)
        super().registrar(conta)