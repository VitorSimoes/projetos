# Faça um programa, com uma função que necessite de três argumentos,
# e que forneça a soma desses três argumentos.

def soma_tres(valor1, valor2, valor3):
    res = valor1 + valor2 + valor3
    return res


valor_1 = int(input("Informe o primeiro valor a ser somado: "))
valor_2 = int(input("Informe o segundo valor a ser somado: "))
valor_3 = int(input("Informe o terceiro valor a ser somado: "))

resposta = soma_tres(valor_1, valor_2, valor_3)

print(resposta)