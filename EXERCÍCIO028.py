# Desafio 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

n = int(input('\nJogo da Adivinhação:\n\n'
                'Entre 0 e 5, em que número estou pensando?'))
l = (0,1,2,3,4,5)

a = random.choice(l)

if n == a:
    print('Parabéns! Você acertou! Eu realmente pensei no número {}.'.format(a))
else:
    print('Você errou. Achou que era {} mas o número que pensei foi {}'.format(n,a))

