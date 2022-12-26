"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
 * salários até R$ 280,00 (incluindo) : aumento de 20%
 * salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
 * salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
 * salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
 * o salário antes do reajuste;
 * o percentual de aumento aplicado;
 * o valor do aumento;
 * o novo salário, após o aumento.
"""

salarioInicial = float(input("Digite o seu salário antes do reajuste: "))

if salarioInicial <= 280.0:
    salarioFinal = salarioInicial * 1.2
    percentual = 20
elif 280.0 < salarioInicial < 700.0:
    salarioFinal = salarioInicial * 1.15
    percentual = 15
elif 700.0 < salarioInicial < 1500.0:
    salarioFinal = salarioInicial * 1.1
    percentual = 10
else:
    salarioFinal = salarioInicial * 1.05
    percentual = 5

print(f'SALÁRIO ANTES DO REAJUSTE: {salarioInicial}')
print(f'PERCENTUAL DO AUMENTO APLICADO: {percentual}')
print(f'VALOR DO AUMENTO: {salarioFinal - salarioInicial}')
print(f'SALÁRIO APÓS O REAJUSTE: {salarioFinal}')