def calcular_media(nota1, nota2):
    """Recebe duas notas e retorna a média aritmética."""
    return (nota1 + nota2) / 2

def verificar_situacao(media):
    """Avalia a média e retorna a situação do aluno segundo critérios do IFPR."""
    if media >= 6.0:
        return "Aprovado"
    elif media >= 4.0:
        return "Recuperação"
    else:
        return "Reprovado"

def solicitar_notas(nome_aluno):
    """Solicita e valida as notas, garantindo que estejam entre 0 e 10."""
    notas = []
    for i in range(1, 3):
        while True:
            try:
                nota = float(input(f"Digite a nota {i} do(a) aluno(a) {nome_aluno}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("  -> Inválido: A nota deve estar entre 0.0 e 10.0.")
            except ValueError:
                print("  -> Erro: Por favor, digite um número válido.")
    return notas[0], notas[1]

def gerar_relatorio(nome, media, situacao):
    """Exibe os dados individuais do aluno de forma formatada."""
    print("-" * 30)
    print(f"Aluno: {nome} | Média: {media:.1f} | Situação: {situacao}")
    print("-" * 30)

def calcular_media_turma(medias, tamanho_total=None):
    """
    Calcula a média geral da turma usando recursão (sem sum ou for).
    A matemática aplicada é: (a + b + c)/3 == (a/3) + (b/3) + (c/3)
    """
    # Define o tamanho original na primeira execução para usar nas divisões
    if tamanho_total is None:
        tamanho_total = len(medias)
        
    # Caso Base: a lista esvaziou, encerra a recursão
    if not medias:
        return 0
        
    # Passo Recursivo: divide o primeiro item pelo total e chama a função para o resto da lista
    return (medias[0] / tamanho_total) + calcular_media_turma(medias[1:], tamanho_total)

def resumo_turma(situacoes):
    """Recebe a lista de situações e retorna a contagem de cada categoria."""
    aprovados = situacoes.count("Aprovado")
    recuperacao = situacoes.count("Recuperação")
    reprovados = situacoes.count("Reprovado")
    
    return aprovados, recuperacao, reprovados

def exibir_relatorio_final(media_geral, aprovados, recuperacao, reprovados):
    """Exibe o relatório consolidado de toda a turma."""
    print("\n" + "="*40)
    print("        RELATÓRIO FINAL DA TURMA")
    print("="*40)
    print(f"Média Geral da Turma : {media_geral:.1f}")
    print(f"Total de Aprovados   : {aprovados}")
    print(f"Total em Recuperação : {recuperacao}")
    print(f"Total de Reprovados  : {reprovados}")
    print("="*40 + "\n")

def main():
    """Programa principal que orquestra as chamadas das funções."""
    print("--- Sistema de Avaliação IFPR ---\n")
    
    # Listas para armazenar os dados da turma
    medias_turma = []
    situacoes_turma = []
    
    # Processa os 3 alunos
    for i in range(3):
        print(f"\n--- Cadastro do {i+1}º Aluno ---")
        nome = input("Digite o nome do aluno: ")
        
        # Coleta e processamento individual
        nota1, nota2 = solicitar_notas(nome)
        media = calcular_media(nota1, nota2)
        situacao = verificar_situacao(media)
        
        # Armazena os dados para o cálculo final da turma
        medias_turma.append(media)
        situacoes_turma.append(situacao)
        
        # Exibe o resultado do aluno atual
        gerar_relatorio(nome, media, situacao)

    # Processamento Final da Turma
    media_geral = calcular_media_turma(medias_turma)
    aprovados, rec, reprovados = resumo_turma(situacoes_turma)
    
    exibir_relatorio_final(media_geral, aprovados, rec, reprovados)

# Execução protegida do arquivo
if __name__ == "__main__":
    main()