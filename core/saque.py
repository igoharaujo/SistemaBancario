from __future__ import annotations
from core.transacao import Transacao

class Saque(Transacao):
    """Transação de saque em uma conta bancária.

    Attributes:
        _valor: Valor a ser sacado.
    """

    def __init__(self, valor):
        """Inicializa a transação de saque.

        Args:
            valor: Valor a ser sacado.
        """
        self._valor = valor

    @property
    def valor(self):
        """float: Valor a ser sacado."""
        return self._valor

    def registrar(self, conta: Conta):
        """Executa o saque e registra a transação no histórico da conta.

        Args:
            conta: Conta na qual o saque será realizado.
        """
        conta.sacar(self._valor)
        super().registrar(conta)