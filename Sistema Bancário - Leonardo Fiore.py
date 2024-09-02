menu= "Bem vindo! Escolha uma das opções a seguir: \n[1] Depositar \n[2] Sacar \n[3] Extrato \n[4] Sair \nOpção: "

saldo = 0
limite_valor = 500
extrato = ""
saques_realizados = 0
limite_de_saque = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor != 0:
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"
            print(f"Deposito realizado com sucesso!")
        
        if valor == 0:
            print("Operação falhou, valor informado inválido!")
            
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        saldo_insuficiente = valor > saldo
        limite_excedido = saques_realizados >= limite_de_saque
        limite_de_valor = valor > limite_valor
        
        if saldo_insuficiente:
            print("Operação falhou! Saldo insuficiente.")

        elif limite_de_valor:
            print("Operação falhou! Limite de valor diário excedido.")

        elif limite_excedido:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques_realizados += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "3":
        print("\n=== Extrato Bancário ===")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

        
            