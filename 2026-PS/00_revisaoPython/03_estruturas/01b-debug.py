# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros porpositais. Encontre e corrija todos:

catalogo = [
    {'titulo': 'Código Limpo', 'autor': 'Robert C. Martins', 'disponivel': True},
    {'titulo': 'Entendendo Algoritmos', 'autor': 'Aditya Bhargava', 'disponivel': False},
    {'titulo': 'Python Fluente', 'autor': 'Luciano Ramalho', 'disponivel': True},
]

print('Primeiro livro:', catalogo[0]['titulo'])

print('\nLivros Disponíveis')
for livro in catalogo:
    if livro['disponivel'] == True:
        print(f' ✅ {livro['titulo']}')

total = len(catalogo)
print(f'\nTotal de livos: {total}')

for chave, valor in catalogo[0].items():
    print(f'{chave}: {valor}')

primeiro_autor = catalogo[0]['autor']
print('\nAutor do primeiro livro:', primeiro_autor)
