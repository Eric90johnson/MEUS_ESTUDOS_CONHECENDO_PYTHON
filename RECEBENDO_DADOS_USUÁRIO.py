"""
Recebendo dados do usário

print('Qual o seu nome?')
nome = input() # Input -> entrada (teclado)

input(-> Todo dado recebido via input é do tipo String

em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples tripla;
- Aspas duplas tripla;

Exemplo:
- Aspas simples -> 'Eric'
- Aspas duplas -> "Eric"
- Aspas simples triplas ->
"""
# """Eric """

# entrada de dados
print('Qual o seu nome?')
nome = input()

# Exemplo antigo do print 'antigo' 2.x
print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
# print(f'Seja bem-vindo(a) {nome}')

print('Qual a sua idade?')
idade = input()

# processamento

# saída de dados
print(' %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
# print(f' {nome} tem {idade} anos')

"""
int(idade) => cast
Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'{nome} nasceu em {2021 - int(idade)}')





