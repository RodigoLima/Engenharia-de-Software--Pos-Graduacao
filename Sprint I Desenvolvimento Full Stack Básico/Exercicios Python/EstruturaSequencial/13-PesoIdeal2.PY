"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

"""


GeneroChar = input(
    "Digite o sexo da pessoa, M para Masculino ou F para Feminino: ")


if GeneroChar in ['M', 'F']:
    AlturaPessoa = float(input("Digite a altura da pessoa: "))

    if GeneroChar == "M":
        PesoIdeal = (72.7 * AlturaPessoa) - 58
    elif GeneroChar == "F":
        PesoIdeal = (62.1 * AlturaPessoa) - 44.7

    print("O peso ideal é: {}".format(PesoIdeal))
else:
    print("Sexo Inválido.")
