# Desafio 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n  = int(input('Digite um valor:'))
n1 = int(input('Digite outro valor:'))

if n > n1:
    print('O primeiro valor é maior.')
elif n < n1:
    print('O segundo valor é maior.')
elif n == n1:
    print('Não existe valor maior, os dois são iguais.')
