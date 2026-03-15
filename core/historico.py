from core.transacao import Transacao

class Historico:
    """Armazena o histórico de transações de uma conta bancária.

    Attributes:
        _transacao: Lista de transações registradas na conta.
    """

    def __init__(self):
        """Inicializa o histórico com uma lista de transações vazia."""
        self._transacao = []

    @property
    def transacao(self):
        """list: Lista de transações registradas."""
        return self._transacao

    def adicionar_transacao(self, transacao: Transacao):
        """Adiciona uma transação ao histórico.

        Args:
            transacao: Transação a ser registrada no histórico.
        """
        self._transacao.append(transacao)