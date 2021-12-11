# Desafio027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Obs: Já use a função .strip() para remover espaços excedentes na variável.
# Se temos, por exemplo, o nome "MARIA DA SILVA" e a gente usa o SPLIT,
# o LEN conta a quantidade de palavras começando, obviamente, no "1":
# MARIA = 1
# DA = 2
# SILVA = 3
# Ou seja, o LEN mostra pra gente que existem 3 palavras.
# MAS na função LISTA, a contagem se inicia no "0".
# A gente usa a LISTA numa variável que já está SPLITADO (nome) como na linha do Gustavo a seguir:
# print('Seu último nome é {}'.format(nome[ len(nome)-1] ))
# print('Seu último nome é {}'.format(nome[ 3 - 1 ]))
# Lembrem-se que a ordem na LISTA da variável (nome) é:
# MARIA = posição 0
# DA = posição 1
# SILVA = posição 2
# Então fazendo o (3 - 1) dentro do parêntesis ficaria:
# print('Seu último nome é {}'.format(nome[2])) que é justamente sempre o último sobrenome nesse exercício.
# Resumo: a função split divide a palavra e conta a partir de zero (0)
# Ex: Anderson (0), Gabriel (1), dos (2), Santos (3)
# Já a função len conta quantos elementos foram divididos
# Ex: Anderson (1), Gabriel (2), dos (3), Santos (4)
# Para identificar o último nome, fazemos a divisão com split, fazemos a contagem de palavras em len - 1 e
# temos o último nome.


n  = str(input('Digite um nome completo:')).strip()
d  = n.split()

print('O primeiro nome é: {}'.format(d[0]))
print('O último nome é: {}'.format(d[len(d) - 1]))

