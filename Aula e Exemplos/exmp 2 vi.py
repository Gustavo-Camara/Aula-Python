salario = float(input("Qual o seu salario: ? "))

if salario <= 2000:
    soma = salario * 0.15
elif salario > 2000:
    soma = salario * 0.10

soma2 = salario + soma
print("O aumento do seu salario irá ser {}".format(soma))
print("Seu salario com o aumento irá ficar {}".format(soma2))