#matematica financeira para terabitia
print('juros simples, juros composto e taxa de juros')

print()

print('Programa de pveno, qualquer duvida me manda mensagem terapia')

print('='*30)
print('juros simples')
print('juros compostos')
print('=' *30)

n = input('Digite a operacao que vc deseja realizar: ')

print()
print('a opcao escolhida foi {}' .format(n))
print()

if n == 'juros simples':
  
  print('a formula para calcular é : J = c*i*t')
  
  print()
  
  print('Digite qual parte da operacao você deseja saber:')
  print()
  print('Se quiser saber o valor do juros, digite : \n"juros"')
  print()
  print('Se quiser saber o valor do tempo em meses, digite: "tempo"')
  print()
  print('Se quiser saber o valor da taxa de juros mensal, digite: "taxajuros" ')
  print()

  entrada1 = input('Digite o que quer descobrir: ')

  if entrada1 == 'juros' :
  
    capital = float(input('Digite o valor do capital inicial: '))
    tempo = float(input('Digite o valor do tempo em meses: '))
    taxa = float(input('Digite a taxa percentual de juros mensal: '))
    taxap = taxa/(100)
    juros = capital*tempo*taxap
    print('O valor do juros é: {} ' .format(juros))

  elif entrada1 == 'tempo':
    capital = float(input('Digite o valor do capital inicial: ' ) )
    juros= float(input('Digite o valor do juros total: ' ) )
    taxa = float(input('Digite a taxa percentual de juros mensal: ' ))
    taxap = taxa/(100)
    tempo = juros/(capital*taxap)
    print('O tempo necessario em meses será de: {}' .format(tempo) )

  elif entrada1 == 'taxajuros':
    capital = float(input('Digite o valor do capital inicial: ' ) )
    juros= float(input('Digite o valor do juros total: ' ) )
    tempo = float(input('Digite o valor do tempo em meses: '))
    taxa = juros/(capital *tempo)
    taxat = taxa*100
    print('A taxa mensal de juros será de: {} %' .format(taxat))
  
elif n == 'juros compostos':
  print()
  print('A formula para calcular juros compostos é:')
  print('M = C * (1 + i)^n ')
  print()
  print('Digite qual parte da operacao você deseja saber:')
  print()
  print('Se quiser saber o valor da taxa de juros mensal, digite : \n"taxajuros"')
  print()
  print('Se quiser saber o valor do tempo em meses, digite: "tempo"')
  print()
  print('Se quiser saber o valor do montante, digite: "montante" ')
  print()
  print('Se quiser saber o valor do capital aplicado, digite: "capital aplicado"')
  print()
  print('Se quiser saber o valor do juros, digite "juros" ')
  print()
  print()

  entrada2 = input("Digite aqui o que você quer saber: ")

  if entrada2 == 'taxajuros':
    montante = float(input('Digite o valor do montante:' ) )
    capital = float(input('Digite o valor do capital aplicado: ') )
    tempo = float(input('Digite o numero de meses: '))
    taxa = (( montante/(capital) ) ** (1/tempo))-1
    taxat = taxa*100
    print('O valor da taxa de juros mensal é: {} % ' .format(taxat) )
  
  elif entrada2 == 'tempo':
    montante = float(input('Digite o valor do montante:' ) )
    capital = float(input('Digite o valor do capital aplicado: ') )
    taxa = float(input('Digite o valor da taxa mensal :' ) )
    taxap = taxa/100
    tempo = (montante/capital*(1+taxap))
    print(tempo)

  elif entrada2 == 'montante':
    capital = float(input('Digite o valor do capital aplicado: ') )
    tempo = float(input('Digite o numero de meses: ') )
    taxa = float(input('Digite o valor da taxa de juros mensal: ') ) 
    taxat = taxa/100
    montante = capital* (taxat+1)**tempo
    print('O valor do montante é de: R${:.2f}' .format(montante) )

  elif entrada2 == 'juros':
    capital = float(input('Digite o valor do capital aplicado: ') )
    tempo = float(input('Digite o numero de meses: ') )
    taxa = float(input('Digite o valor da taxa de juros mensal: ') )
    taxap = taxa/100 
    juros = capital * ((1+taxap) - 1 )
    print('O valor do juros acumulado é de: R$ {:.2f}' .format(juros))