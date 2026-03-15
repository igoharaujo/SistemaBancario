from core.pessoa_fisica import PessoaFisica
from core.contacorrente import ContaCorrente
from core.historico import Historico
from core.deposito import Depositar
from core.saque import Saque

clientes = []


def menu():
    print("""
========================================
         SISTEMA BANCÁRIO
========================================
[1] Novo cliente
[2] Nova conta corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar clientes
[7] Listar contas
[0] Sair
----------------------------------------""")
    return input("=> ").strip()


def novo_cliente():
    cpf = input("CPF: ").strip()
    if _buscar_cliente(cpf):
        print("! CPF já cadastrado.")
        return
    nome = input("Nome: ").strip()
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ").strip()
    endereco = input("Endereço: ").strip()
    cliente = PessoaFisica(endereco=endereco, cpf=cpf, nome=nome, data_nascimento=data_nascimento)
    clientes.append(cliente)
    print(f"Cliente '{nome}' cadastrado com sucesso.")


def nova_conta():
    cpf = input("CPF do titular: ").strip()
    cliente = _buscar_cliente(cpf)
    if not cliente:
        print("! Cliente não encontrado.")
        return
    historico = Historico()
    conta = ContaCorrente.nova_conta(cliente, historico=historico)
    cliente.adicionar_conta(conta)
    print(f"Conta {conta.numero} criada para {cliente.nome} | Agência: {conta.agencia}")


def depositar():
    cpf = input("CPF do titular: ").strip()
    cliente = _buscar_cliente(cpf)
    if not cliente:
        print("! Cliente não encontrado.")
        return
    conta = _selecionar_conta(cliente)
    if not conta:
        return
    try:
        valor = float(input("Valor do depósito: R$ ").replace(",", "."))
    except ValueError:
        print("! Valor inválido.")
        return
    if valor <= 0:
        print("! O valor deve ser positivo.")
        return
    cliente.realizar_transacao(conta, Depositar(valor))
    print(f"Depósito de R$ {valor:.2f} realizado. Saldo: R$ {conta.saldo:.2f}")


def sacar():
    cpf = input("CPF do titular: ").strip()
    cliente = _buscar_cliente(cpf)
    if not cliente:
        print("! Cliente não encontrado.")
        return
    conta = _selecionar_conta(cliente)
    if not conta:
        return
    try:
        valor = float(input("Valor do saque: R$ ").replace(",", "."))
    except ValueError:
        print("! Valor inválido.")
        return
    if valor <= 0:
        print("! O valor deve ser positivo.")
        return
    saldo_antes = conta.saldo
    cliente.realizar_transacao(conta, Saque(valor))
    if conta.saldo < saldo_antes:
        print(f"Saque de R$ {valor:.2f} realizado. Saldo: R$ {conta.saldo:.2f}")
    else:
        print("! Saldo insuficiente. Operação não realizada.")


def extrato():
    cpf = input("CPF do titular: ").strip()
    cliente = _buscar_cliente(cpf)
    if not cliente:
        print("! Cliente não encontrado.")
        return
    conta = _selecionar_conta(cliente)
    if not conta:
        return
    transacoes = conta.historico.transacao
    print(f"\n--- Extrato | Conta {conta.numero} ---")
    if not transacoes:
        print("  Nenhuma transação registrada.")
    else:
        for i, t in enumerate(transacoes, 1):
            tipo = type(t).__name__
            print(f"  {i}. {tipo:<10} R$ {t.valor:.2f}")
    print(f"  Saldo atual: R$ {conta.saldo:.2f}")
    print("-------------------------------")


def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n--- Clientes ---")
    for c in clientes:
        print(f"  {c.nome} | CPF: {c.cpf} | Contas: {[ct.numero for ct in c.contas]}")


def listar_contas():
    todas = [(c, ct) for c in clientes for ct in c.contas]
    if not todas:
        print("Nenhuma conta cadastrada.")
        return
    print("\n--- Contas ---")
    for cliente, conta in todas:
        print(f"  Nº {conta.numero} | Ag: {conta.agencia} | Titular: {cliente.nome} | Saldo: R$ {conta.saldo:.2f}")


def _buscar_cliente(cpf):
    for c in clientes:
        if c.cpf == cpf:
            return c
    return None


def _selecionar_conta(cliente):
    if not cliente.contas:
        print("! Este cliente não possui contas.")
        return None
    if len(cliente.contas) == 1:
        return cliente.contas[0]
    print("Contas disponíveis:")
    for i, c in enumerate(cliente.contas, 1):
        print(f"  [{i}] Conta {c.numero} | Saldo: R$ {c.saldo:.2f}")
    try:
        idx = int(input("Escolha: ")) - 1
        return cliente.contas[idx]
    except (ValueError, IndexError):
        print("! Opção inválida.")
        return None


acoes = {
    "1": novo_cliente,
    "2": nova_conta,
    "3": depositar,
    "4": sacar,
    "5": extrato,
    "6": listar_clientes,
    "7": listar_contas,
}

while True:
    opcao = menu()
    if opcao == "0":
        print("Encerrando...")
        break
    acao = acoes.get(opcao)
    if acao:
        acao()
    else:
        print("! Opção inválida.")
