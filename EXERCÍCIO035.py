# Desafio  035: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
# Condições: a + b > c; b + c > a; a + c > b.

a = int(input('Primeiro segmento:'))
b = int(input('Segundo segmento:'))
c = int(input('Terceiro segmento:'))

if a + b > c and b + c > a and a + c > b:
    print('Com essas medidas será possível formar um triângulo.')
else:
    print('Não será possível formar um triângulo com essas medidas.')



