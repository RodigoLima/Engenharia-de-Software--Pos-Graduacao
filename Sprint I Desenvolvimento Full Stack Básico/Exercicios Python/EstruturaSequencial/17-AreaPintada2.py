"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

area_pintar = float(
    input("Digite tamanho em metros quadrados da area a ser pintada: "))

cobertura_tinta_litros = (area_pintar / 6) * 1.1

quantidade_latas_tinta = math.ceil(cobertura_tinta_litros / 18)

quantidade_galoes_tintas = math.ceil(cobertura_tinta_litros / 3.6)

valor_total_latas = quantidade_latas_tinta * 80

valor_total_galoes = quantidade_galoes_tintas * 25

quantida_lata_mista = round((cobertura_tinta_litros / 18), 0)

resto_latas_mista = cobertura_tinta_litros - (quantida_lata_mista * 18)

# resto do que vai ser supridos pelas as latas#
quantidade_galoes_misto = math.ceil(resto_latas_mista / 3.6)

valor_total_misto = (quantida_lata_mista * 80) + \
    (quantidade_galoes_misto * 3.6)

if resto_latas_mista > 0:  # nao precisa compra misto#
    print(
        f'Comprando misto, deve-se comprar {quantida_lata_mista} latas e {quantidade_galoes_misto} galao no valor total: {valor_total_misto} R$')

print(
    f'Comprando apenas latas de tinta, vai ser preciso de: {quantidade_latas_tinta} lata(s) no valor total de: {valor_total_latas} R$')

print(
    f'Comprando apenas galoes de tinta, vai ser preciso de: {quantidade_galoes_tintas} galao(oes) no valor total de: {valor_total_galoes} R$')
