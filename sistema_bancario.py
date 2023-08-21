def menu():
    
    print("=" * 10, 'BANCO', "=" * 10)
    print('''
    [1] Depositar    
    [2] Sacar  
    [3] Extrato
    [4] Sair
    ''')
    print("=" * 27)   
    
    
def sacar(saldo, extrato, tentativas_saque, LIMITE_TENTATIVAS, limite):
    # Teste valor de saldo, se o valor de saque ultrapassa o limite e as tentativas
    try:
        print(F'Saldo: R$ {saldo:.2f}')
        valor_saque = float(input('Saque: '))
        if valor_saque >= 0.1:
            if valor_saque > saldo:
                print('Falha: Parece que você não possui saldo sufisciente para saque.')
                return saldo, extrato, tentativas_saque
            elif valor_saque > limite:
                print('Falha: Parece que o valor de saque ultrapassa o valor maximo de R$ 500.')
                return saldo, extrato, tentativas_saque
            
            elif tentativas_saque >= LIMITE_TENTATIVAS:
                print('Falha: Parece que você excedeu o número maximo de saques diários.')
                return saldo, extrato, tentativas_saque
            else:
                saldo -= valor_saque
                tentativas_saque += 1
                extrato += f'Saque: R$ {valor_saque:.2f}\n'
                print(f'Sucesso: Valor de R$ {valor_saque} sacado com sucesso!!!')
                return saldo, extrato, tentativas_saque
        else:   
            print('Falha: O valor de saque deve ser maior que zero.')
            return saldo, extrato, tentativas_saque
        
    except ValueError:
        print('Erro: Insira um valor número válido.')
        return saldo, extrato, tentativas_saque
    
def depositar(novo_saldo, extrato):
    try:
        deposito = float(input('Depositar: '))
        if deposito > 0.0:
            novo_saldo += deposito
            extrato += f'Depositou: R$ {deposito:.2f}\n'
            print(f'Sucesso: Valor de R$ {novo_saldo} depositado com sucesso!!!')
            return novo_saldo, extrato
        else:
            print('Falha: Insira um valor válido.')
            return novo_saldo, extrato
    except ValueError:
        print('Erro: Parece que você não informou um valor.')
        return novo_saldo, extrato
    
def vizualizar_extrato(extrato, saldo):
    print("=" * 10, 'EXTRATO', "=" * 10)
    for ext in extrato.split('\n'):
        if ext:
            print(ext)

            
    print(f'Saldo atual: R$ {saldo:.2f}')
    print("=" * 20)
    
def sair():
    quit()
    

def banco():
    saldo = 0
    extrato = ""
    tentativas_saque = 0
    LIMITE_TENTATIVAS = 3 
    limite = 500
    
    while True:
        menu()
        print()
        
        escolha = input('Escolha: ')
        
        if escolha == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif escolha == '2':
            saldo, extrato, tentativas_saque = sacar(saldo, extrato, tentativas_saque, LIMITE_TENTATIVAS, limite)
            
        elif escolha == '3':
            vizualizar_extrato(extrato, saldo)
            
        elif escolha == '4':
            sair()
            
        else:
            print('Falha: Opção inválida.')
  

if __name__ == "__main__":
    banco()