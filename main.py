import random
x = int(input('Ile faktów dodać?:'))
fakty = []
for i in range(x):
    fakt = input('Podaj fakt:')
    fakty.append(fakt)
print('Twoja prawda to:', random.choice(fakty))
