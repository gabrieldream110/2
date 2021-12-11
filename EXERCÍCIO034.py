# Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

s  = float(input('Salário de funcionário:'))

s1 = s + (s * (10/100))
s2 = s + (s * (15/100))

if s > 1250.00:
    print('Para salário de R$ {}, acima do teto de R$ 1250.0 o aumento será de 10%, \ncom valor final de {}R$ {}{}.'.format(s,'\033[32m',s1,'\033[m'))
else:
    print('Para salários com teto até R$ 1250.00, sendo o do funcionário em questão igual a R$ {},\no aumento será de 15%, com valor final de {}R$ {}{}.'.format(s,'\033[32m',s2,'\033[m'))

