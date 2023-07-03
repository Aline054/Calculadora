def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Função principal da calculadora
def calculadora():
    print("Bem-vindo à calculadora!")
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada: ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = soma(num1, num2)
            print("Resultado: ", resultado)
        elif escolha == '2':
            resultado = subtracao(num1, num2)
            print("Resultado: ", resultado)
        elif escolha == '3':
            resultado = multiplicacao(num1, num2)
            print("Resultado: ", resultado)
        elif escolha == '4':
            resultado = divisao(num1, num2)
            print("Resultado: ", resultado)
    else:
        print("Escolha inválida. Por favor, tente novamente.")

# Executar a calculadora
calculadora()
