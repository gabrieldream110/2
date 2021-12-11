# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

n   = str(input('Digite um nome completo:'))
div = n.split()
pn  = div[0]
pn1 = len(pn)
n0  = n.count(' ')
n1  = len(n)
ss  = n1 - n0


print('Nome completo em maiúsculo: {}{}{}'.format('\033[32m',n.upper(),'\033[m'))
print('Nome completo em minúsculo: {}{}{}'.format('\033[32m',n.lower(),'\033[m'))
print('Letras ao todo sem espaços: {}{}{}'.format('\033[32m',ss,'\033[m'))
print('Letras no primeiro nome: {}{}{}'.format('\033[32m',pn1,'\033[32m'))
