# SISTEMA DE ARMAZENAMENTO 
# Disciplina: Programação de Sistemas (PS)
# Aula: 05 Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor: Artur Lacerda da SIlva
# Data: 2026/02/26
# Repositório: https://github.com/20251CTB0100004-spec/2026-PS

# DESCRIÇÃO:
# Este programa analiza o estoque de uma biblioteca e permite ao usuário cadastrar novos livros.


catalogo = [
    {'titulo' : 'Volta ao mundo em 80 dias', 'autor' : 'Julio Verne', 'ano' : 1872, 'status' : 'disponível'},
    {'titulo' : 'Dom Casmurro', 'autor' : 'Machado de Assis', 'ano' : 1899, 'status' : 'disponível'},
    {'titulo' : 'O Pequeno Príncipe', 'autor' : 'Antoine de Saint-Exupery', 'ano' : 1943, 'status' : 'disponível'},
    {'titulo' : '1984', 'autor' : 'George Orwell', 'ano' : 1948, 'status' : 'disponível'},
    {'titulo' : 'O Senhor dos Anéis', 'autor' : 'J.R.R. Tolkien', 'ano' : 1954, 'status' : 'disponível'},
]


def MostrarCatalogo():
    print('=== Catálogo de Livros ===')
    for livro in catalogo:
        print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']}) - {livro['status']}")


def contagem():
    contagem = 0
    contagemdisp = 0
    for contagemlivros in catalogo:
        contagem += 1
        if contagemlivros['status'] == 'disponível':
            contagemdisp += 1
    print('\n=== Contagem de Livros ===')    
    print(f"Total de livros no catálogo: {contagem}")
    print(f'Total de livros disponíveis: {contagemdisp}')


def Main():
    while True:

        print('Deseja cadastrar um novo livro? (s/n)')
        opcao = input().lower()
        if opcao == 's':
            titulo = input('Digite o título do livro: ')
            autor = input('Digite o autor do livro: ')
            ano = int(input('Digite o ano do livro: '))
            catalogo.append({'titulo' : titulo, 'autor' : autor, 'ano' : ano, 'status' : 'disponível'})
        else:
            print('\nEncerrando o programa. Até mais!\n')
            MostrarCatalogo()
            contagem()
            break

        print('=== Catálogo de Livros ===')
        MostrarCatalogo()
        

print('Bem vindo à Arturteca Livros!')
MostrarCatalogo()
Main()