# SISTEMA DE BIBLIOTECAS 
# Disciplina: Programação de Sistemas (PS)
# Aula: 05 Revisão: Estruturas de Dados, Listas e Dicionários
# Autor: Artur Lacerda da SIlva
# Data: 2026/03/12
# Repositório: https://github.com/20251CTB0100004-spec/2026-PS

# DESCRIÇÃO:
# Catálogo de livros que demonstra o uso de listas e dicionários para armazenar informações

# BASICOS: listas e manipulações
titulos = [
    'O Programador Pragmatico',
    'Codigo Limpo',
    'Entendendo Algoritmos',
]

print('Primeiro livro:', titulos[0])
print('Último livro:', titulos[-1])
print('Total de livros:', len(titulos))

print('Operações na lista')

# Adicinar um livro pro final da lista
titulos.append('Python fluente')
print('Lista após adicionar um livro:', titulos)

# Verificar se um livro está na lista
busca = 'Codigo Limpo'
if busca in titulos:
    print(f'O livro "{busca}" está na lista.')
else:    
    print(f'O livro "{busca}" não está na lista.')

# Ordenar lista
titulos.sort()
print('Lista ordenada:', titulos)

# Remover um livro da lista
titulos.remove('Entendendo Algoritmos')
print('Lista após remover um livro:', titulos)

print('\n')
# DICIONARIOS: conceitos básicos

# dicionario com um livro e seus atributos
livro = {
    'titulo': 'O Programador Pragmatico',
    'autor': 'Andrew Hunt', 
    'ano': 1999, # int
    'disponivel': True, # bool
}

# acessando o dicionario pelas chaves
print('Título: ', livro['titulo'])
print('Autor: ', livro['autor'])
print('Ano: ', livro['ano'])
print('Status: ', 'disponível' if livro['disponivel'] else 'emprestado')

print("\n")
# MODIFICANDO E CONSULTANDO

# atualizendo um valor existente
livro['disponivel'] = False #livro foi emprestado
print('\nApós empréstimo:', livro['disponivel'])

# adiconando uma nova chave
livro['paginas'] = 352
print('Páginas:', livro['paginas'])

# .get() - acesso seguro: retorna None (ou padrao) se a chave não existir
editora = livro.get('editora', 'Não informada')
print('Editora:', editora)

print('\n')

# LISTA DE DICIONÁRIOS (catalogo)

catalogo = [
    {'titulo': 'O Programador Pragmático', 'autor': 'Andrew Hunt', 'ano': 1999, 'disponivel': True},
    {'titulo': 'Códgio Limpo', 'autor': 'Roberto C. Martin', 'ano': 2008, 'disponivel': False},
    {'titulo': 'Entendendo Algoritmos', 'autor': 'Aditya Bhargava', 'ano': 2016, 'disponivel': True},
]

print('=== Catálogo da Biblioteca ===')
print()

# percorrendo com for:
for livro in catalogo:
    status = 'Disp' if livro['disponivel'] else 'Emprestado'
    print(f' {livro['titulo']} ({livro["ano"]})')
    print(f' Autor: {livro["autor"]} | {status}')
    print(' ' + '-' * 40)

print('\n')

# CONSULTAS E FILTROS

print('\n=== Livros disponíveis ===')
for livro in catalogo:
    if livro['disponivel']:
        print(f'{livro["titulo"]}')

print('\n=== Busca por título ===')
busca = input('Digite o título (ou parte)').lower()
encontrado = False
for livro in catalogo:
    if busca in livro['titulo'].lower():
        print(f' Encontrado: {livro['titulo']} - {livro["autor"]}')
        encontrado = True
if not encontrado:
    print(' Nenhum livro encontrado com esse termo.')

print('\n=== Atributos do primeiro livro ===')
for chave, valor in catalogo[0].items():
    print(f' {chave}: {valor}')

