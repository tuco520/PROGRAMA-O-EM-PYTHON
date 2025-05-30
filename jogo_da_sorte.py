import random

numero_sorte = random.randint(1,10)
meu_numero = int(input('digite seu numero da sorte: '))
if numero_sorte == meu_numero:
    print ('você sortudo(a), acertou em cheio!')
else:
        print ('você errou feio, não sabe escolher :  o numero é', numero_sorte)
        