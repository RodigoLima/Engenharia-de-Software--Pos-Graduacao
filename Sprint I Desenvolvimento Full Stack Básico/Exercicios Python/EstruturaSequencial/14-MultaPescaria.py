"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

"""


Peso_Peixe_Caputurado = float(input("Digite o peso do Peixe: "))

Peso_Limite_Peixe = 50; # Pode ser que mude a regulamentacao #
Multa_Kg_Excedente = 4 # Pode mudar #

if Peso_Peixe_Caputurado <= Peso_Limite_Peixe:
    print("Peso do Peixe de acordo com a regulamentação.")
else:
    ExcessoPeixe =  Peso_Peixe_Caputurado - Peso_Limite_Peixe;
    MultaExcesso = (ExcessoPeixe * Multa_Kg_Excedente)
    print("Peso do peixe em desacordo com a regulamentacao, multa no valor de: {} R$ por {} Kg Excedente".format(MultaExcesso,ExcessoPeixe))