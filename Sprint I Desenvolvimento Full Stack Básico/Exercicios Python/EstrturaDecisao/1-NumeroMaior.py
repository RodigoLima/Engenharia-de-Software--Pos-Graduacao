"""

Faça um Programa que peça dois números e imprima o maior deles.

"""

num1 = float(input("Digite o primeiro numero: "))

num2 = float(input("Digite o segundo numero: "))


if num1 > num2:
    maior_numero = num1
elif num2 > num1:
    maior_numero = num2
else:
    print("O numero são iguais")
    exit()

print(f'O maior numero é: {maior_numero}')