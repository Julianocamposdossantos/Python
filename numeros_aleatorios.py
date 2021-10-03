import random

print('Números Aleatórios')

numero1 = ['1', '2', '3']

numero2 = ['4', '5', '6']

numero3 = ['7', '8', '9']

aleatorio1 = random.choice(numero1)

aleatorio2 = random.choice(numero2)

aleatorio3 = random.choice(numero3)

resultado = aleatorio1 + ' ' + aleatorio2 + ' ' + aleatorio3

print(resultado)
