# SISTEMA DE CÁLCULO DE IMC
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisao: Funcoes
# Autor      : Artur Lacerda Silva
# Data       : 2026/03/14
# Repositorio: https://github.com/20251ctb0100004-spec/2026-PS
# 
# DESCRIÇÃO: 
# Calcula e classifica o IMC de uma pessoa
# Demosntra fefinição de funções, parâmetros, retorno, escopo e recursão 


# FUNÇÃO SEM PARÂMETROS OU RETORNO

def exibir_cabecalho():
    '''Exibe o cabeçalho do sistema no terminal.''' # docstring: documentação da função 
    print('=' * 40)
    print('    SISTEMA DE CÁLCULO DE IMC')
    print('=' * 40)

# chama a função
exibir_cabecalho()   

def exibir_rodape():
    print('=' * 40)
    print('    SISTEMA ENCERRADO')
    print('=' * 40)

exibir_rodape()

# FUNÇÃO COM PARÂMETROS E RETORNO

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc 

peso = float(input('Peso (kg): '))
altura = float(input('altura (m): '))

resultado = calcular_imc(peso, altura)
print(f'Seu IMC é: {resultado:.2f}')

# ESCOPO LOCAL vs GLOBAL

versao = '1.0'

def demonstrar_escopo():
    mensagem = 'Olá do interior da função'
    print(f' mensagem = {mensagem}')
    print(f' versao = {versao}')

demonstrar_escopo()

print('\nFora da função')
print(f' versao = {versao}')


# VALOR PADRÃO E MÚLTIPLOS RETORNOS
"""Classifica o IMC e retorna classificação e emoji de status. 
Parâmetro 'unidade' tem valor padrão - não é obrigatório informar'"""
def classificar_imc(imc, unidade='kg/m²'):
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
        emoji = '⬇'
    elif imc < 25.0:
        classificacao = 'Peso normal'
        emoji = '✅'
    elif imc < 30.0:
        classificacao = 'Sobrepeso'
        emoji = '⚠'
    else:
        classificacao = 'Obesidade'
        emoji = '🔴'

    return classificacao, emoji

# chamda sem o parâmetro opcional (usa o padrão 'kg/m²')
imc_teste = 22.5
classificacao, emoji = classificar_imc(imc_teste)
print(f'IMC {imc_teste} ({classificacao}) {emoji}')

# chamda informando o parâmetro opcional 
classificacao, emoji = classificar_imc(imc_teste, unidade='lb/in²')
print(f'Mesma chamada com unidade custimizada: {classificacao} {emoji}')


# RECURSÃO BÁSICA

def contagem_regressiva(n):
    if n < 0:
        return
    print(n)
    contagem_regressiva(n - 1)

print('\nContagem regressiva')
contagem_regressiva(5)


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

print('\nFatorial')
for i in range(1, 7):
    print(f' {i}! = {fatorial(i)}')


# FUNÇÃO PRINCIPAL

def processar_pessoa():
    nome = input("\nNome: ")
    peso = float(input('Peso (kg): '))
    altura = float(input('Altura (kg): '))

    imc = calcular_imc(peso, altura)
    classificacao, emoji = classificar_imc(imc)

    print("\nRESULTADO")
    print(f'Nome          : {nome}')
    print(f'IMC           : {imc:.2f} kg/m²')
    print(f'Classificação : {classificacao} {emoji}')


# EXECUÇÃO PRINCIPAL

exibir_cabecalho()

continuar = 's'
while continuar == 's':
    processar_pessoa()
    continuar = input('\nProcessar outra pessoa [s]/[n]: ').lower()

exibir_rodape()