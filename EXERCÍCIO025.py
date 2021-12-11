# Desafio 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# Problema: Como faço quando há nomes semelhantes, como Silvana, Silvani?
# Solução: O mais simples foi, ao pedir o programa para localizar 'Silva' pôr um espaço ' ' na frente do nome.
# Mesmo que peçam para dividir o nome em split, o programa lerá os nomes na variáve inicial
# e sempre, após o nome, haverá um espaço separando as palavras, o que não acontece com Silvana, Silvani etc
# cujo nome está junto de outras letras.

n = str(input('Digite um nome:'))
d = n.split()

print(d)

print('O nome acima tem o sobrenome Silva. Verdadeiro (True) ou Falso (False)?\n{}'.format('Silva ' in n))
