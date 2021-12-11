# Desafio 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v  = float(input('Radar Eletrônico\n\n'
                'Velocidade Registrada: '))
vm = float(input('Velocidade Máxima Permitida na Via: '))
mu = (v - vm) * 7.00

if v > vm:
    print('\033[31mO veículo trafegou acima da velocidade máxima permitida: {} Km/h. \n'
          'Portanto o condutor foi sujeito à penalização por multa de\033[m {}R$ {}{}'.format(v,'\033[32m',mu,'\033[m'))
else:
    print('\033[32mO veículo trafegou dentro do limite de velocidade máxima permitida: {}{}{} Km/h.\n'
          'Fica, assim, livre de quaisquer penalidades legais.\033[m '.format('\033[30m',v,'\033[m'))
