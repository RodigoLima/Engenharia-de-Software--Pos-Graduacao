
"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

Primeiro_Numero = int (input("Digite o primeiro numero inteiro: "))

Segundo_Numero = int (input("Digite o segundo numero inteiro: "))

Terceiro_Numero = float(input("Digite o terceiro numero Real: "))


Produto_Dobro = (Primeiro_Numero * (Segundo_Numero * 0.5 ) ) # o produto do dobro do primeiro com metade do segundo .

SomaTriplo = ( ( Primeiro_Numero * 3 ) + Terceiro_Numero ) # a soma do triplo do primeiro com o terceiro.

TerceiroCubo = ( Terceiro_Numero ** 3 ) #o terceiro elevado ao cubo.

print("O produto do dobro do primeiro com metade do segundo: {}".format(Produto_Dobro))

print("A soma do triplo do primeiro com o terceiro: {}".format(SomaTriplo))

print("O terceiro elevado ao cubo: {}".format(TerceiroCubo))