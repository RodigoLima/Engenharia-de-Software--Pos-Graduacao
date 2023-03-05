"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

"""

AlturaPessoa = float(input("Digite a altura da pessoa: "))

PesoIdealCalc = (72.7 * AlturaPessoa) - 58

print("O pessoa ideal é: {}".format(PesoIdealCalc))