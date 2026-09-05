#include <stdio.h>
void main()
{
    int idade;
    int possui;
    printf("Digite sua idade: ");
    scanf("%d", &idade);
    printf("Possui titutlo de eleitor? (1 - Sim / 0 - Nao): ");
    scanf("%d", &possui);
    if (possui || idade < 16)
    {
        printf("Voce nao pode votar .\n");
    
    
        else if (idade <16 && possui == 1)
        {
            printf("Acreano.\n");
        }
    }
    else
    {
        if (idade >= 16 && idade < 18)
        {
            printf("Voto opcional.\n");
        }
        else if (idade >= 18 && idade < 69)
        {
            printf("Voto obrigatorio.\n");
        }
        else
        {
            printf("Voto facultativo.\n");
        }
    }
    
}