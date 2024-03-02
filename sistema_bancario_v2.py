def menu():
    menu = """
    ================= MENU ================

    Escolha a opção desejada

    [D ] Depósito
    [S ] Saque
    [E ] Extrato
    [NU] Novo Usuário
    [NC] Nova Conta
    [LC] Listar Contas
    [Q ] Sair

    """
    return input(menu).upper()


def depositar(saldo, deposito, extrato, /):
    if deposito <= 0:
        print("Operação Inválida")

    else:
        saldo += deposito
        extrato += f"Depósito \tR${deposito:.2f}\n"
        print(f"Depósito efetuado no valor de \tR${deposito:.2f}")

    return saldo, extrato


def sacar(*, saque, saques_efetuados, saldo, extrato, LIMITE_SAQUES, LIMITE):
    if saques_efetuados == LIMITE_SAQUES:
        print("Limite diário de saques atingido!")

    elif saque > LIMITE:
        print("Valor acima do limite permitido!")

    elif saldo < saque:
        print("Saldo insuficiente!")

    else:
        saldo -= saque
        extrato += f"Saque \tR${saque:.2f}\n"
        saques_efetuados += 1
        print(f"Saque efetuado no valor de \tR${saque:.2f}")

    return saldo, extrato, saques_efetuados


def tira_extrato(saldo, /, *, extrato):
    if not extrato:
        print("Não foram realizadas movimentações.\n")
        print(f"Saldo Atual: \tR${saldo:.2f}\n")
    else:
        print(f"{extrato} \nSaldo Atual: \tR${saldo:.2f}\n")
    return extrato, saldo


def linha():
    print("=" * 50)


def novo_usuario(usuarios):
    cpf = input("CPF (apenas números): ")

    fluxo = validar_cpf(usuarios, cpf)

    if fluxo:
        return

    nome = input("Nome: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Logradouro, n°- Bairro - Cidade/UF : ")

    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})

    print("\nCadastro realizado com sucesso!")

    return usuarios


def validar_cpf(usuarios, cpf):
    user = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if user:
        print("\nCPF já cadastrado! Usuário já existente!")
        linha()
        return user


def criar_conta(usuarios, numero_conta, contas):
    cpf = input("Digite o CPF(apenas números): ")
    usuario = validar_cpf(usuarios, cpf)

    if not usuario:
        print("\nUsuário não encontrado!")

    else:
        AGENCIA = "0001"
        numero_conta += 1
        cliente = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        nome_usuario = cliente[0]['nome']

        contas.append({"agencia":AGENCIA,
                       "cc":numero_conta,
                       "cliente":nome_usuario
                      })
        print("Conta criada com sucesso!")
    
    return numero_conta, contas


def listar_contas(contas):
    for conta in contas:
        linha =f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['cc']}
        Titular:\t{conta['cliente']} 
    
        """
        print(linha)


def main():
    saldo = 0
    LIMITE = 500
    saques_efetuados = 0
    LIMITE_SAQUES = 3
    extrato = ""
    usuarios = []
    contas = []
    numero_conta = 0

    while True:
        opcao = menu()

        if opcao == "D":
            print(" Depósito ".center(50, "="))

            deposito = int(input("Valor do Depósito: "))

            saldo, extrato = depositar(saldo, deposito, extrato)
            linha()

        elif opcao == "S":
            print(" Saque ".center(50, "="))

            saque = int(input("Valor do Saque: "))

            saldo, extrato, saques_efetuados = sacar(
                saque=saque,
                saques_efetuados=saques_efetuados,
                saldo=saldo,
                extrato=extrato,
                LIMITE_SAQUES=LIMITE_SAQUES,
                LIMITE=LIMITE
            )

            linha()

        elif opcao == "E":
            print(" Extrato ".center(50, "="))

            extrato, saldo = tira_extrato(saldo, extrato=extrato)
            linha()

        elif opcao == "Q":
            linha()
            print("Sua sessão foi encerrada. Tenha um bom dia!\n")
            break

        elif opcao == "NU":
            print(" Novo usuário ".center(50, "="))
            novo_usuario(usuarios)
            linha()

        elif opcao == "NC":
            print(" Nova Conta ".center(50, "="))
            numero_conta, contas = criar_conta(usuarios, numero_conta, contas)

        elif opcao == "LC":
            print(" Listar Contas ".center(50, "="))
            listar_contas(contas)
    
        else:
            linha()
            print("Opcão Inválida!")


main()
