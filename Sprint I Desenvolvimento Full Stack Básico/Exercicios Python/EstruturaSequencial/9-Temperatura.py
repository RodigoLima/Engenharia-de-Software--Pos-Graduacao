"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

F = float(input("Digite o valor da TEMPERATURA EM FAREHAIT: "))

C = 5 * ((F-32) / 9)


print("A temperatura em farenhait {} corresponde a {} celcius".format(F,C))