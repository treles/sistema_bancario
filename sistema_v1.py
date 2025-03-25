menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito"))
        
        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"
            
        else:
            print("Operaçao façhou o valor informado e invalido")
           
    elif opcao == "s":
        valor = float(input("Informe o valor do saque"))
       
        excedeu_saldo = valor > saldo
      
        excedeu_limite = valor > limite
      
        excedeu_saques = numero_saques >= LIMITE_SAQUES
     
        if excedeu_saldo:
            print("Operaçao falhou! Voce nao tem saldo suficiente.")
                         
        elif excedeu_limite:
            print("Operaçao falhou! O valor do saque excede o limite.")
            
        elif excedeu_saques:
            print("Operaçao falhou! Numero maximo de saques excedido.")
            
        else:
            print("Operaçao falhou! o valor informado e invalido.")
            
    elif opcao == "e":
        print("\n============== EXTRATO ===================")
        print("Nao foram realizadas movimentaçoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operaçao invalida, por favor selecione novamente a operaçao desejada.")        
                                     