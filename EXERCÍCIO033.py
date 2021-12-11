# Desafio 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# A maneira mais simples de fazer estará nos comentários:
#
# Identificando menor número:
# menor = a
# if b < a and b < c:
#       menor = b
# if c < a and c < b:
#       menor = c
#
# Identificando menor número:
# maior = a
# if b > a and b > c:
# maior = b
# if c > a and c > b:
# maior = c
# print('Número menor {}\nNúmero menor {}'.format(menor,maior))

a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))

s1 = a > b > c
s2 = a > c > b
s3 = b > a > c
s4 = b > c > a
s5 = c > a > b
s6 = c > b > a

if s1:
    print('Valor maior {}\nValor menor {}'.format(a,c))
if s2:
    print('Valor maior {}\nValor menor {}'.format(a,b))
if s3:
    print('Valor maior {}\nValor menor {}'.format(b,c))
if s4:
    print('Valor maior {}\nValor menor {}'.format(b,a))
if s5:
    print('Valor maior {}\nValor menor {}'.format(c,b))
if s6:
    print('Valor maior {}\nValor menor {}'.format(c,a))
