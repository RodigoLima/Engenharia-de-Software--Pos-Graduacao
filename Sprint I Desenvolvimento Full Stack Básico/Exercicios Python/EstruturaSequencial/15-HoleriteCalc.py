"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$  
    Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

Hora_Trabalhada = int(input("Digite o numero de horas trabalhadas: "))

Valor_Hora = float(input("Digite o valor por hora trabalhada: "))

Salario_Bruto = Valor_Hora * Hora_Trabalhada

IR = (11 / 100) # 11% #

INSS = ( 8 / 100 ) # 8% #

Dsc_Per_Sindicato = ( 5 / 100 ) # 5%$

Dsc_Vlr_INSS = (Salario_Bruto * INSS)

Dsc_Vlr_IR =   ( (Salario_Bruto - Dsc_Vlr_INSS ) * IR  )  # IR NAO INCIDE SOBRE DESCONTO DO INSS

Dsc_Vlr_Sindicato =  ( ( Salario_Bruto - Dsc_Vlr_INSS - Dsc_Vlr_IR  ) * Dsc_Per_Sindicato) 

DescontosTotal = Dsc_Vlr_INSS + Dsc_Vlr_IR + Dsc_Vlr_Sindicato

Salario_Liquido = Salario_Bruto - DescontosTotal

print("+ Salário Bruto : {:.2f} R$".format(Salario_Bruto))
print("- IR (11%) : {:.2f} R$".format(Dsc_Vlr_IR))
print("- INSS (8%) : {:.2f} R$".format(Dsc_Vlr_INSS))
print("- Sindicato (5%) : {:.2f} R$".format(Dsc_Vlr_Sindicato))
print("= Salário Liquido : {:.2f} R$".format(Salario_Liquido))
