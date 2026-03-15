from __future__ import annotations
from abc import ABC


class Transacao(ABC):
    """Classe abstrata base para transações bancárias."""

    def registrar(self, conta: Conta):
        """Registra a transação no histórico da conta.

        Args:
            conta: Conta na qual a transação será registrada.
        """
        conta.historico.adicionar_transacao(self)