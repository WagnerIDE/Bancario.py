def main():
    saldo = 0
    limite = 500.00
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        print("\n=== MENU ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")
            else:
                print("Valor inválido para depósito!")

        elif opcao == "2":
            if numero_saques >= LIMITE_SAQUES:
                print("Limite diário de saques excedido!")
                continue

            valor = float(input("Digite o valor do saque: R$ "))
            
            if valor > limite:
                print(f"Valor excede o limite de R$ {limite:.2f} por saque!")
            elif valor > saldo:
                print("Saldo insuficiente para realizar o saque!")
            elif valor <= 0:
                print("Valor inválido para saque!")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")

        elif opcao == "3":
            print("\n=== EXTRATO ===")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print(extrato)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print(f"Número de saques realizados hoje: {numero_saques}/{LIMITE_SAQUES}")

        elif opcao == "4":
            print("Obrigado por usar nosso sistema!")
            break

        else:
            print("Opção inválida! Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()