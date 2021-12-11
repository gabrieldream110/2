# Desafio 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

n = str(input('Digite o nome de uma cidade:'))
d = n.split()
s = d[0]
print('O nome dessa cidade começa com a palavra Santo. Falso(False) ou verdadeiro (True)?'
      '\n{}'.format('Santo' in s))
