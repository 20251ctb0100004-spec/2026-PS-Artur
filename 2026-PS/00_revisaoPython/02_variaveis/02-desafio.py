# SISTEMA DE ARMAZENAMENTO 
# Disciplina: Programação de Sistemas (PS)
# Aula: 04 Revisão: Variáveis, Tipos de Dados e Controle de Dados
# Autor: Artur Lacerda da SIlva
# Data: 2026/02/26
# Repositório: https://github.com/20251CTB0100004-spec/2026-PS

# DESCRIÇÃO: Estoque de uma loja 


estoque = [
    {'produto' : 'mouse', 'qtd' : 1},
    {'produto' : 'RAM 16gb', 'qtd' : 2},
    {'produto' : 'RAM 4gb', 'qtd' : 3},
    {'produto' : 'RAM 8gb', 'qtd' : 4},
    {'produto' : 'cabo', 'qtd' : 5},
]
global critico, adequado, excesso

critico = 0
adequado = 0
excesso = 0

def mostrar_estoque():

    print('===== Estoque completo: =====')
    for item in estoque:
        if item['qtd'] < 5:
            print(f'Produto: {item['produto']} Situação: Crítica')
            global critico
            critico += 1
        elif item['qtd'] < 20:
            print(f'Produto: {item['produto']} Situação: Adequada')
            global adequado
            adequado += 1
        else:
            print(f'Produto: {item['produto']} Situação: Excesso')
            global excesso
            excesso += 1
    print('==============================')

def main():
    while True:
        print('=== Lista de opções: ===')
        print('[1] Mostrar o estoque\n[2] Adicionar ao estoque\n[3] Pegar do estoque\n[4] Sair\n=======================')
        escolha = input('Digite a opção desejada: \n')
        
        if escolha == '1':
            mostrar_estoque()
        elif escolha == '2':
            produto = input('Digite o nome do produto: ')
            qtd = int(input('Digite a quantidade a ser adicionada: '))
            global critico, adequado, excesso
            estoque.append({'produto': produto, 'qtd': qtd})
            print(f'Produto {produto} adicionado com sucesso!')
        elif escolha == '3':
            produto = input('Digite o nome do produto: ')
            qtd = int(input('Digite a quantidade a ser retirada: '))
            for item in estoque:
                if item['produto'] == produto:
                    if item['qtd'] >= qtd:
                        item['qtd'] -= qtd
                        print(f'Produto {produto} retirado com sucesso!')
                    else:
                        print('Quantidade insuficiente em estoque.')
                    break
            else:
                print('Produto não encontrado.')
        elif escolha == '4':
            print('Até mais!')
            print(f'Produtos em situação crítica: {critico}')
            print(f'Produtos em situação adequada: {adequado}')
            print(f'Produtos em situação de excesso: {excesso}')
            break
        else:
            print('Opção inválida. Tente novamente.')

main()