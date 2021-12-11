# Desafio 039: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#
# O período de Alistamento Militar inicia no primeiro dia útil do mês de janeiro e vai até
# o último dia útil de junho.
# O jovem deve se alistar no ano em que completar 18 anos,
# na Junta de Serviço Militar mais próxima de sua residência.

import datetime

d  = int(input('Bem vindo ao Departamento de Alistamento Militar!\nNos informe sua data de nascimento abaixo:\n'
              'Dia: '))
an = int(input('\nAno de nascimento:'))
mc = int(input('\nMês de cadastro:'))
co = 2020 - an
cm = 17 - co


if co == 17 and mc < 7:
    print('Você está na idade certa para alistamento e dentro do prazo mensal para fazer o cadastro.')
elif co == 17 and mc > 6:
    print('Você está na idade certa para alistamento mas o prazo mensal expirou. Dirija - se à unidade mais próxima.')
elif co < 17:
    print('Falta ainda {} anos para seu alistamento ser realizado.'.format(cm))
elif co > 17:
    print('Você está acima da idade para alistamento. Caso ainda não o tenha feito dirija - se ao departamento.')



