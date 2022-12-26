"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
 * "Telefonou para a vítima?"
 * "Esteve no local do crime?"
 * "Mora perto da vítima?"
 * "Devia para a vítima?"
 * "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

telefonou = input("Telefonou para a vítima? [S]im/[N]ão ")
telefonou = telefonou.upper()

noLocal = input("Esteve no local do crime? [S]im/[N]ão ")
noLocal = noLocal.upper()

moraPerto= input("Mora perto da vítima? [S]im/[N]ão ")
moraPerto = moraPerto.upper()

eraDevedor = input("Devia para a vítima? [S]im/[N]ão ")
eraDevedor = eraDevedor.upper()

trabalhou = input("Já trabalhou com a vítima? [S]im/[N]ão ")
trabalhou = trabalhou.upper()

quantPositivas = 0

if telefonou == 'S':
    quantPositivas += 1
if noLocal == 'S':
    quantPositivas += 1
if moraPerto == 'S':
    quantPositivas += 1
if eraDevedor == 'S':
    quantPositivas += 1
if trabalhou == 'S':
    quantPositivas += 1

if quantPositivas == 2:
    print("SUSPEITO!")
elif quantPositivas == 3 or quantPositivas == 4:
    print("CÚMPLICE!")
elif quantPositivas == 5:
    print("ASSASSINO!")
else:
    print("INOCENTE!")