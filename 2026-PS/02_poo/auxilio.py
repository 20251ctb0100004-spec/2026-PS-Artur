def teste_inicio():
    # Atributos originais
    nome = input('nome')
    especie = input('especie')
    idade = input('idade')
    # Novos atributos
    peso = float(input("peso"))
    vacinado = input("vacinado")
    dono = input('dono')
    # Atributo de controle de estado
    hospedado = False

def exibir_dados():
    print("\n--- Dados do Pet ---")
    print(f"Nome: {nome}")
    print(f"Espécie: {especie}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")
    print(f"Dono: {dono}")
    status_vacina = "Sim" if vacinado else "Não"
    print(f"Vacinado: {status_vacina}")
    status_hospedagem = "Hospedado" if hospedado else "Não hospedado"
    print(f"Status: {status_hospedagem}")
    print("-" * 20)

    exibir_dados()

teste_inicio()
pet = ("Rex", "Cachorro", 5, 15.5, True, "João")