"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta
a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

areaMetrosQuadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litrosNecessarios = areaMetrosQuadrados/6
litrosNecessarios = litrosNecessarios * 1.1

if litrosNecessarios % 18:
    quantLatas = litrosNecessarios//18 + 1
else:
    quantLatas = litrosNecessarios/18
gastoLatas = quantLatas * 80

print(f'QUANTIDADE DE LATAS = {quantLatas} => R${gastoLatas}')

if litrosNecessarios % 3.6:
    quantGaloes = litrosNecessarios//3.6 + 1
else:
    quantGaloes = litrosNecessarios/3.6
gastoGaloes = quantGaloes * 25

print(f'QUANTIDADE DE GALÕES = {quantGaloes} => R${gastoGaloes}')

quantMisturaLata = litrosNecessarios//18

if ((litrosNecessarios - quantMisturaLata) % 3.6):
    quantMisturaGalao = ((litrosNecessarios - quantMisturaLata*18) // 3.6) + 1
else:
    quantMisturaGalao = ((litrosNecessarios - quantMisturaLata*18) // 3.6)
gastoMisturaLata = quantMisturaLata * 80
gastoMisturaGalao = quantMisturaGalao * 25

print(f"MISTURANDO LATAS E GALÕES, TEREMOS: {quantMisturaLata} LATAS e {quantMisturaGalao} GALÕES => R${gastoMisturaLata} em latas e R${gastoMisturaGalao} em galões => TOTAL = {gastoMisturaLata + gastoMisturaGalao}")