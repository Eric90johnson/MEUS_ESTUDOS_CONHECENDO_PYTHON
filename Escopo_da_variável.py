"""
Escopo de vaiáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende
    todo programa.

2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarado.

Para declarar variáveis em Python fazemos:

nome_da_variável = valor_da_variável

ex.:
numero = 42 # exemplo de variável global.
print(numero)

if numero > 10: # Exemplo de variável local.
    novo = numero + 10
    print(novo)

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Esse tipo é inferido ao atribuirmos o valor a mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42

"""