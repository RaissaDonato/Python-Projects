""" Calculadora com while """


while True:
    a = input("Digite o primeiro número: ")
    b = input("Digite o segundo número: ")
    op = input("Digite o operador que você deseja utilizar (+, -, /, *): ")

    numeros_validos = None

    try:
        a_float = float(a)
        b_float = float(b)
        numeros_validos = True
    except:
        numeros_validos = None
        print("Erro!")

    if numeros_validos is None:
        print("Você inseriu números inválidos!")
        continue

    op_validos = "+-/*"

    if op not in op_validos:
        print("Operador inválido!")
        continue

    if len(op) > 1:
        print("Digite apenas um operador!")

    if op == "+":
        soma = a_float + b_float
        print(f'{a_float} {op} {b_float} = {soma}')

    elif op == "-":
        sub = a_float - b_float
        print(f'{a_float} {op} {b_float} = {sub}')

    elif op == "/":
        div = a_float/b_float
        print(f'{a_float} {op} {b_float} = {div}')

    else:
        mult = a_float * b_float
        print(f'{a_float} {op} {b_float} = {mult}')
    executar = input("Você deseja executar a operação? ([s]im ou n[ão]): ")
    executar = executar.lower()

    if executar == "n":
        break
    else:
        continue