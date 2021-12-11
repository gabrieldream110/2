# Desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# O que eu aprendi: É possível usar a divisão inteira e por meio do módulo resto da divisão podemos fazer.
# Exemplificando: o comando '//' significa divisão inteira
# O comando %10 divide o número por 10 e mostra o resto da divisão.
# Ex: 1923 // 1 % 10 (1923 divisão inteira por um, exiba o resto da divisão por 10)
# dá um valor inteiro, sobrando 3, que é o resto da divisão.
# Assim consigo definir, pela divisão inteira com o módulo do resto da divisão(%) o número que quero exibir.
# É possível particionar, ou dividir, um número usando a matemática.

n = int(input('Digite um número de 0 a 9999:'))

u = n // 1    % 10
d = n // 10   % 10
c = n // 100  % 10
m = n // 1000 % 10

print('Analizando o número {} temos que:'.format(n))
print('Sua unidade é: {}{}{}'.format('\033[32m',u,'\033[m'))
print('Sua dezena é: {}{}{}'.format('\033[32m',d,'\033[m'))
print('Sua centena é: {}{}{}'.format('\033[32m',c,'\033[m'))
print('Seu milhar é: {}{}{}'.format('\033[32m',m,'\033[m'))
