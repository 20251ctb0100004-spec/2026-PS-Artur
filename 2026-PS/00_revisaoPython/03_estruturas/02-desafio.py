# SISTEMA DE ARMAZENAMENTO 
# Disciplina: Programação de Sistemas (PS)
# Aula: 05 Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor: Artur Lacerda da SIlva
# Data: 2026/02/26
# Repositório: https://github.com/20251CTB0100004-spec/2026-PS

# DESCRIÇÃO:
# Este programa analiza o estoque de uma biblioteca e permite ao usuário cadastrar novos livros.


catalogo = [
    {'titulo' : 'volta ao mundo em 80 dias', 'autor' : 'julio Verne', 'ano' : 1872, 'status' : 'disponível'},
    {'titulo' : 'dom casmurro', 'autor' : 'machado de assis', 'ano' : 1899, 'status' : 'disponível'},
    {'titulo' : 'o pequeno príncipe', 'autor' : 'antoine de saint-exupery', 'ano' : 1943, 'status' : 'disponível'},
    {'titulo' : '1984', 'autor' : 'george orwell', 'ano' : 1948, 'status' : 'disponível'},
    {'titulo' : 'o senhor dos anéis', 'autor' : 'j.r.r. tolkien', 'ano' : 1954, 'status' : 'disponível'},
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


def buscarLivro(titulo):
    for livro in catalogo:
        if livro['titulo'] == titulo or livro['autor'] == titulo:
            return livro
        print(livro)
    return None


def Main():
    while True:
        
        print('\nDeseja cadastrar um novo livro? [1]\nDeseja buscar um livro? [2]\nDeseja sair? [3]')
        opcao = int(input())
        if opcao == 1:
            titulo = input('Digite o título do livro: ').lower
            autor = input('Digite o autor do livro: ').lower
            ano = int(input('Digite o ano do livro: '))
            catalogo.append({'titulo' : titulo, 'autor' : autor, 'ano' : ano, 'status' : 'disponível'})
        elif opcao == 2:
            titulo = input('Digite o título ou autor do livro: ').lower
            livro = buscarLivro(titulo)
            if livro:
                print(f"\nLivro encontrado: {livro['titulo']} - {livro['autor']} ({livro['ano']}) - {livro['status']}")
            else:
                print("\nLivro não encontrado.")
        elif opcao == 3:
            print('\nEncerrando o programa. Até mais!\n')
            MostrarCatalogo()
            contagem()
            break

        

print('Bem vindo à Arturteca Livros!')
MostrarCatalogo()
Main()

