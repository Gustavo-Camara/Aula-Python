n1 = int(input("Digite um numero"))
n2 = int(input("Digite outro numero"))
n3 = int(input("Digite outro numero"))

if n1 <= 0 or n2 <= 0 or n3 <= 0:
    print("Digite apenas numeros maiores que zero!")    

elif n1 >= n2 and n1 >= n3:
    print("N1 É MAIOR QUE N2 E N3")
    if n2 >= n3:         
        print(n1,n2,n3)
        print("O menor é n3:{}".format(n3))
    else:
        print(n1,n3,n2)
        print("O menor é n2:{}".format(n2))
elif n2 >= n1 and n2 >= n3:
    print("N2 é maior que n1 e N3")
    if n1 >= n3:
        print(n2,n1,n3)
        print("O menor é n3:{}".format(n3))
    else:
        print(n2,n3,n1)
elif n3 >= n1 and n3 <= n2:
    print("N3 é o maior que n1 e n2 ")
    if n1 >= n2:
        print(n3,n1,n2)
        print("O menor é n2:{}".format(n2))
    else:
        print(n3,n2,n1)
        print("O menor é n1:{}".format(n1))