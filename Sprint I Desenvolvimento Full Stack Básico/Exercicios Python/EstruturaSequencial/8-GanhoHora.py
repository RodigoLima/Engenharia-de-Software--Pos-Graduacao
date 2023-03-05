"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

"""


ganho_hora = float(input("Digite o valor da sua hora: "))
num_hora = float(input("Digite o numero de horas trabalhadas: "))

renda = ganho_hora * num_hora


print("O total do salario é: {}".format(renda))


