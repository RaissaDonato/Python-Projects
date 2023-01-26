import random

cpf = ""
for i in range(9):
    cpf += str(random.randint(0, 9))

cont = 10
soma = 0

for digito in cpf[0:9]:
    soma = soma + int(digito) * cont
    cont = cont - 1

soma = soma * 10
resto = soma % 11

if resto > 9:
    d1 = 0
else:
    d1 = resto

cpf += str(d1)

soma = 0
cont = 11

for digito in cpf[0:10]:
    soma = soma + int(digito) * cont
    cont = cont - 1

soma = soma * 10
resto = soma % 11

if resto > 9:
    d2 = 0
else:
    d2 = resto

cpf += str(d2)

print(cpf)