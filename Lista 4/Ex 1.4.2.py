velocidade = float(input("Qual a velocidade do carro? "))
limite = float(input("Qual o limite de velocidade? "))

if velocidade > 1.2 * limite:
    print("Infração grave")
elif velocidade > limite:
    print("Infração média")
else:
    print("DENTRO DO LIMITE")