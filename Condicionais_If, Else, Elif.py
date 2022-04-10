"""
Estruturas condicionais
If (Se), else (outro), elif (else + if)

If (SE)

Ex. Estrutura condicional if, else em C

if(idade < 18){
    printf("Menor de idade");
}else if(idade ==18){
    printf("Tem 18 anos");
}else{
    printf("Maior de idade");
}

Ex. Estrutura condicional if, else em Java

if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade ==18){
    System.out.println("Tem 18 anos");
}else{
    System.out.println("Maior de idade");
}

Ex. ELIF

Não existem nas linguagens de programação tipo C e JAVA
"""

idade = 18

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('tem 18 anos')
else:
    print('Maior de idade')
