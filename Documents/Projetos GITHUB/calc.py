while True:
  n1=float(input('Digite um nunero: '))
  n2=float(input('Digite um nunero: '))
  print('1- Soma')
  print('2- Subtracao')
  print('3- Multiplicacao')
  print('4- Divisao')
  print('5- Sair')
  opcao=input('Escolher uma opcao: ')
  if opcao == '1':
    resultado=n1+n2
    print(f'O resultado é : {resultado} ')
  elif opcao == '2':
    resultado=n1-n2
    print(f'O resultado é : {resultado} ')
  elif opcao == '3':
    resultado=n1*n2
    print(f'O resultado é : {resultado} ')
  elif opcao == '4':
    resultado=n1/n2
    print(f'O resultado é : {resultado:.2f} ')
  elif opcao =='5':
    print('Operacao Encerrada')
    break
  else:
    print('Operacao Invalidade')
