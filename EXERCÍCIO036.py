# Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from math import ceil
v  = float(input('\033[34mAnálise de Financiamento\n\nValor do imóvel:\033[m'))
s  = float(input('\n\033[34mSalário do comprador:\033[m'))
p  = int(input('\n\033[34mTotal de Parcelas:\033[m'))
a  = p * (1/12)
pr = v * (1/p)
lp = s * (30/100)
e  = v * (30/100)
v1 = v - e
n = float(input('\033[34m\nPossível valor de entrada:\033[m'))
nf = (v - n)/p
na = n * ((1 / v) * 100)


if pr > lp:
    print('\nSujeitando o cliente à análise, concluímos que:'
          '\nCom salário de {}R${}{}\nCom prestação de {}R${:.2f}{}, '
          'cujo valor é maior do que a condição para aprovação:'
          '\nPrestações de até, no máximo, 30% do salário '
          '(que seria até {}R${}{}), \nconsiderando também que levará {:.2f} anos para pagar:'
          '\nConcluímos que:\n\nO Financiamento será \n\033[31mRECUSADO\033[m'
          .format('\033[32m',s,'\033[m','\033[31m',pr,'\033[m','\033[32m',lp,'\033[m',ceil(a)))
elif pr > lp:
    n = float(input('\033[34mTente novamente com um valor de entrada:\033[m'))
    nf = (v - n)/p
    na = n * ((1 / v) * 100)
    print('\nValor da nova presatação: {}R${}{}'.format('\033[32m',na,'\033[m'))
elif na > lp:
    print('Analisando a nova simulação temos que:'
          '\nO cliente dará {}R${}{} de entrada, que equivale a {}% do valor do veículo,\n'
          'reduzindo a prestação para {}R${}{}, ainda acima do valor mínimo permitido.\n'
          'Portanto o financiamento foi:'
          '\n\033[31mRECUSADO\033[m'.format('\033[32m',n,'\033[m',na,'\033[32m',nf,'\033[m'))
else:
    print('Valor de Entrada: {}{}{}\n'
          'Parcelas: {}\n'
          'Valor de parcelamento: {}{}{}\n'
          'Análise de Financiamento:\n\n'
          '\033[35mAPROVADO!\033[m'.format('\033[32m',n,'\033[m',p,'\033[32m',nf,'\033[m'))
