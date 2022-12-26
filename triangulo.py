"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
"""

lado1 = float(input("LADO 1: "))
lado2 = float(input("LADO 2: "))
lado3 = float(input("LADO 3: "))

if (((lado1 + lado2) > lado3) and ((lado2 + lado3) > lado1) and ((lado1 + lado3) > lado2)):
    print("Os valores digitados PODEM formar um triângulo!")
    if (lado1 == lado2 and lado2 == lado3):
        print("O triângulo é EQUILÁTERO!")
    elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("O triângulo é ISÓSCELES!")
    else:
        print("O triãngulo é ESCALENO!")
else:
    print("Os valores digitados NÃO PODEM formar um triângulo!")
