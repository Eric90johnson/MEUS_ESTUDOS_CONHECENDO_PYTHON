"""
PEPE8 - Python Enhancement Proposal

São propostas  de melhorias para a linguagem Python

The Zen of Python
import this
A idéia da PEPE8 é que possamos escrever códigos Python de forma Pythônica

[1] - utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes minusculos, separdos por underline ou variáveis;

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identificação!(NÃO USE TAB)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em  branco
Separar funções e definicões de classe com duas linhas em branco;
Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports
imports devem ser sempre feitos em linhas separadas;

# import errado
import sys, os

# import certo
import sys
import os

# Não há problema em utilizar:
from types StringType, ListType

# Caso tenha muitos imports de um mesmo pacote , recomenda-se fazer:

from types import (
    Stringstype,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings
# Antes de contantes ou variáveis globais.

[6] Espaços em expressões e intrunções

# Incorreto:
função( algo[ 1 ], { outro: 2 } )

# Correto:

função(algo[1], {outro: 2})

# Incorreto
algo (1)

# Correto
algo(1)

# Incorreto
dict ['chave'] = lista [indice]

# Correto['chave'] = lista[indice]

# Incorreto:
x              = 1
y              = 5
variavel_longa = 5

# Correto:
x = 1
y = 3
variavel_longa = 5

[7] Termine sem uma instrução com uma linha em branco;
# Exemplo
import this

print('Algo')

"""
import this



