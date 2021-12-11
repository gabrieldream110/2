# Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

n = str(input('Digite um nome completo:'))
a = n.lower()


print('Quantas vezes aparece a letra A em maiúsculo? {}'.format(n.count('A')))
print('Quantas vezes aparece a letra a seja maiúsculo ou minúsculo? {}'.format(a.count('a')))
print('Em que posição, no índice, aparece a letra (a) pela primeira vez? {}'.format(a.find('a')))
print('Em que posição a mesma aparece pela última vez? {}'.format(a.rfind('a')))
