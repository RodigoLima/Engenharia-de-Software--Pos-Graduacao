"""
  Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.  
"""
import math

area_pintar = float(
    input("Digite tamanho em metros quadrados da area a ser pintada: "))

cobertura_tinta_litros = math.ceil(area_pintar / 3)
quantidade_lata = math.ceil(cobertura_tinta_litros / 18)
preco_total = quantidade_lata * 80

print(
    f'A quantidade de latas a serem compradas sao: {quantidade_lata}, no valor total de: {preco_total} R$')
