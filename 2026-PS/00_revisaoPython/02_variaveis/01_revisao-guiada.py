#SISTEMA DE APROVAÇÃO DE ALUNOS
# Disciplina: Programação de Sistemas (PS)
#Aula: 04 Revisão: Variáveis, Tipos e Controle de Fluxo
#Autor: Artur Lacerda da SIlva
#Data: 2026/02/26
#Repositório: https://github.com/20251CTB0100004-spec/2026-PS

# DESCRIÇÃO:
# Este programa processa as notas de uma turma e determina
# a situação de cada aluno (Aprovado, Recuperação ou Reprovado).
# Conceitos utilizados: variáveis, tipos de dados, operadores,
# estruturas de seleção e estruturas de repetição.

# TURMA:
nome = 0
nota1=0
nota2=0

turma = [
    {"nome": "Ana", "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Carla", "nota1": 2.0, "nota2": 3.5},
]
print('==== Resultado da Turma ====')

continuar = 's'
while continuar == 's':
    print('Deseja continuar? (s/n)')
    continuar = input().lower()
    if continuar != 's':
        break
        
    print("=== Sistema de Aprovação de Alunos ===")
    print() # linha em branco para organizar a saída
    nome = input('Digite o nome do aluno: ')
    #str texto
    nota1 = float(input('Digite a nota 1: '))
    # float = decimal
    nota2= float(input('Digite a nota 2: '))
    # float = decimal

    # PROCESSAMENTO
    media = (nota1 + nota2) / 2 #operador aritmético: soma e divisão
    print()
    print (f"Aluno : {nome}")
    print (f"Nota 1: {nota1:.1f}")
    print (f"Nota 2: {nota2:.1f}")
    print (f"Média : {media:.2f}")
    #.2f exibe com 2 casas decimais

    # DECISAO
    if nota1 < 2.0:
        print("⚠️ Atenção: nota muito baixa em uma das avaliações.")
    elif nota2 < 2.0:
        print("⚠️ Atenção: nota muito baixa em uma das avaliações.")

    if media >= 6.0:
        situacao = '✅ Aprovado'
    elif media >= 4.0:
        situacao = '⚠️ Recuperação'
    else:
        situacao = '❌ Reprovado'



    print(f'Situação: {situacao}')
    print('='*40)