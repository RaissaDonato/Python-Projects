"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
"""

valorSaque = int(input("SAQUE MŃIMO: 10 REAIS\n"
                       "SAQUE MÁXIMO: 600 REAIS\n"
                       "Digite o valor que você deseja sacar: "))

if valorSaque < 10 or valorSaque > 600:
    print("Valor de saque inválido!")
else:
    notas100 = valorSaque // 100
    notas50 = (valorSaque % 100) // 50
    notas10 = ((valorSaque % 100) % 50) // 10
    notas5 = (((valorSaque % 100) % 50) % 10) // 5
    notas1 = ((((valorSaque % 100) % 50) % 10) % 5) // 1

    print(f'{notas100} NOTAS DE 100\n'
          f'{notas50} NOTAS DE 50\n'
          f'{notas10} NOTAS DE 10\n'
          f'{notas5} NOTAS DE 5\n'
          f'{notas1} NOTAS DE 1')