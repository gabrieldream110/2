# Desafio 037: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n  = int(input('Digite um número:'))
print('''Escolha uma das bases para conversão para esse número abaixo:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
op = int(input('\nQual a sua escolha?'))

if op == 1:#Na linguagem Python, o número convertido em Binário sempre aparece com 0b na frente.
    print('A conversão do número {} para Binário é igual a: {}'.format(n,bin(n)[2:]))
elif op == 2:# 0o colado ao número quando convertido em Octal.
    print('A conversão do número {} para Octal é igual a: {}'.format(n,oct(n)[2:]))
elif op == 3:#Na linguagem Python, o valor 0xn, quer dizer que o número foi convertido para hexadecimal.
    print('A conversão do número {} para Hexadecimal é igual a: {}'.format(n,hex(n)[2:]))
else:
    print('\nOpção inválida. Tente novamente.')

# Para remover as letras e exibir só os números, podemos usar o fatiamento e fazer a leitura a partir do ídice 2,
# sempre a partir do primeiro número.

