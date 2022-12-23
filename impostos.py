"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto
quanto pagou ao INSS
quanto pagou ao sindicato
o salário líquido
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

salarioHora = float(input("Informe quanto você ganha por hora: "))
horasTrabalhadas = int(input("Informe quantas horas você trabalha por mês: "))

salarioBruto = salarioHora * horasTrabalhadas
valorINSS = (8 * salarioBruto)/100
valorSindicato = (5 * salarioBruto)/100
valorIR = (11 * salarioBruto)/100
salarioLiquido = salarioBruto - (valorIR + valorSindicato + valorINSS)

print(f'SALÁRIO BRUTO: R${salarioBruto:.2f}')
print(f'INSS: R${valorINSS:.2f}')
print(f'IMPOSTO DE RENDA: R${valorIR:.2f}')
print(f'SINDICATO: R${valorSindicato:.2f}')
print(f'SALÁRIO LÍQUIDO: R${salarioLiquido:.2f}')