#Crie um programa que leia a media de um aluno e diga-se ele foi excelente (9-10), bom (7-8.9) ou reprovado (<7)

media = float(input('Digite sua media: '))

if  media > 9 and media <= 10:
    print("Excelente")
elif media > 7 and media < 8.9:
    print("BOM")
elif media < 7:
    print("Reprovado")