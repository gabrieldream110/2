# Desafio 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
m  = (n1 + n2)/2
a  = 'O aluno foi aprovado.'
b  = 'O aluno está de recuperação.'
c  = 'O aluno foi reprovado.'

if m < 5:
    print('Média {}. {}'.format(m,c))
elif m > 5.0 and m < 6.9:
    print('Média {}. {}'.format(m,b))
elif m >6.9:
    print('Média {}. {}'.format(m,a))
