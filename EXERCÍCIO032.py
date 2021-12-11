# Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

a   = int(input('Digite um ano:'))
an  = a // 1 % 400
an1 = a // 1 % 4

if an and an1 == 0:
    print('O ano {} é BISSEXTO.'.format(a))
else:
    print('O ano {} não é BISSEXTO.'.format(a))
