from core.pessoa_fisica import PessoaFisica
from core.contacorrente import ContaCorrente
from core.historico import Historico
from core.deposito import Depositar
from core.saque import Saque


# --- Criação do cliente ---
igor = PessoaFisica(
    endereco="Brasilia",
    cpf="092.456.744.01",
    nome="igor",
    data_nascimento="1999-01-01",
)

# --- Criação da conta corrente ---
historico = Historico()
conta = ContaCorrente.nova_conta(igor, historico=historico)
igor.adicionar_conta(conta)

# --- Exibe dados do cliente ---
print("=== Cliente ===")
print(f"Nome:            {igor.nome}")
print(f"CPF:             {igor.cpf}")
print(f"Endereço:        {igor.endereco}")
print(f"Data nascimento: {igor.data_nascimento}")

# --- Exibe dados da conta ---
print("\n=== Conta Corrente ===")
print(f"Número:  {conta.numero}")
print(f"Agência: {conta.agencia}")
print(f"Saldo:   R$ {conta.saldo:.2f}")
print(f"Limite:  R$ {conta.limite:.2f}")
print(f"Saques permitidos: {conta.saques}")

# --- Realiza transações ---
print("\n=== Transações ===")

deposito = Depositar(1000.0)
igor.realizar_transacao(conta, deposito)
print(f"Depósito de R$ 1000.00 → Saldo: R$ {conta.saldo:.2f}")

saque = Saque(200.0)
igor.realizar_transacao(conta, saque)
print(f"Saque de R$ 200.00   → Saldo: R$ {conta.saldo:.2f}")

saque_invalido = Saque(5000.0)
igor.realizar_transacao(conta, saque_invalido)
print(f"Saque de R$ 5000.00  → Saldo: R$ {conta.saldo:.2f}  (saldo insuficiente, sem efeito)")

# --- Exibe histórico ---
print("\n=== Histórico ===")
for i, t in enumerate(conta.historico.transacao, 1):
    tipo = type(t).__name__
    print(f"  {i}. {tipo} - R$ {t.valor:.2f}")

# --- Exibe contas vinculadas ao cliente ---
print(f"\nContas de {igor.nome}: {[c.numero for c in igor.contas]}")
