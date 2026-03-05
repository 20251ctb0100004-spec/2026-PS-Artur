'''
Aluno: Artur Lacerda da Silva
Data: 02/24/2026
Objetivo: Criar um programa de calculadora, que efetue a soma, subtração, multiplicação, divisão, com meu interativo
'''

def soma():
    print('O seu resultado é: ', A+B)

def sub():
    print('O seu resultado é: ', A-B)

def mult():
    print('O seu resultado é: ', A*B)

def div():
    print('O seu resultado é: ', A/B)

def entrada():
    global A, B
    A = float(input('Digite o primeiro numero: '))
    B = float(input('Digite o segundo numero: '))
    if (op == 4):
        if(B == 0):
            print('Não é possivel dividir por zero! Tente outro numero')
            B = float(input('Digite outro número: '))


def cabecalho():
    while True:
        print('\nESTE É O PROGRAMA ARTUR-CALCULATOR, LISTA DE AÇÕES:\n')
        print('[0] Sair\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n')
        global op
        op = int(input('Escolha sua operação\n'))
        if(op == 0):
            print('Tchau!')
            break
        entrada()
        

        if(op == 1):
            soma()
        elif(op == 2):
            sub()
        elif(op == 3):
            mult()
        elif(op == 4):
            div()
        else:
            print('Entrada invalida')

cabecalho()