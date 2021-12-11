# Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

d = float(input('Agência de Turismo\n'
                'Olá! Obrigado por contar com nosso conforto e segurança para realizar sua viagem!\n'
                'Por favor, defina a distância da Viagem em Km:'))
print('O custo da viagem de {} Km será de: R$ {}'.format(d,d * 0.45) if d > 200 else '\nO custo para percorrer {} Km será de {}'.format(d,d * 0.5))
