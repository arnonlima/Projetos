def soma(n1,n2):
    return (n1+n2)
def subtracao(n1,n2):
    return (n1-n2)
def multiplicacao(n1,n2):
    return (n1*n2)
def divisao(n1,n2):
    return (n1/n2)
def potencia(n1,n2):
    return (n1**n2)
while True:
    n1=float(input('Digite um número: '))
    n2=float(input('Digite um numero: '))
    
    print('1 - Soma')
    print('2 - Subttação')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potencia')
    opcao=input('Escolher uma opcao: ')
    
    if opcao == '1':
        resultado=soma(n1,n2)
        print(f'Resultado é {resultado:.2f}')
    elif opcao == '2':
        resultado=subtracao(n1,n2)
        print(f'Resultadp é {resultado:.2f}')
    elif opcao == '3':
        resultado=multiplicacao(n1,n2)
        print(f'Resultado é {resultado:.2f}')
    elif opcao =='4':
        resultado=multiplicacao(n1,n2)
        print(f'Resultado é {resultado:.2f}')   
    elif opcao =='5':
        resultado=potencia(n1,n2)
        print(f'Resultado é {resultado:.2f}')
            
    else:
        print('Operacao Invalida')