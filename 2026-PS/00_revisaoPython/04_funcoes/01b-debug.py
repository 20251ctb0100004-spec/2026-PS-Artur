# Arquivo: 01b-debug.py
# Corrigido!

def saudacao(nome, turno='manhã'):
    mensagem = f'Bom {turno}, {nome}!'
    return mensagem

# Erro 1 corrigido: Adicionado print para exibir o retorno
print(saudacao('Ana')) 
print(saudacao('Bruno', 'tarde'))

def dobrar(x):
    resultado = x * 2
    return resultado

print('dobro de 5: ', dobrar(5))

total = 0
def incrementar():
    global total  # Erro 2 corrigido: Definindo acesso à variável global
    total = total + 1
    return total

incrementar()
print('Total:', total)

def contagem(n):
    # Erro 3 & 4 corrigidos: Adicionada condição de parada (Base Case)
    if n < 0:
        return
    print(n)
    contagem(n - 1)

contagem(3)