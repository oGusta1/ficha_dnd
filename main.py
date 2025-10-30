from back_end import *

def escolher_opcao(prompt, opcoes):

    print(prompt)
    for i, op in enumerate(opcoes, 1):
        print(f"{i}) {op}")
    while True:
        escolha = input("Escolha pelo número: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return opcoes[int(escolha) - 1]
        print("Opção inválida, tente novamente.")

def distribuir_atributos(valores_disponiveis, nomes_atributos):

    restantes = valores_disponiveis[:]
    alocados = {}
    print("\nDistribua os atributos usando os valores:", restantes)
    for nome in nomes_atributos:
        while True:
            print(f"\nAtribuindo para {nome} | Disponíveis: {restantes}")
            valor = input(f"Digite um valor para {nome}: ").strip()
            if not valor.isdigit():
                print("Digite um número inteiro.")
                continue
            valor = int(valor)
            if valor not in restantes:
                print("Valor não disponível. Escolha um da lista.")
                continue
            alocados[nome] = valor
            restantes.remove(valor)
            break
    return alocados

def main():
    print("=== Criador de Ficha D&D ===\n")

    nome = input("Nome do personagem: ").strip()
    if not nome:
        nome = "SemNome"

    racas = ["Humano", "Elfo", "Anão", "Halfling", "Meio-Orc"]
    raca = escolher_opcao("\nEscolha a raça:", racas)

    classes = ["Ladino", "Guerreiro", "Bárbaro"]
    classe = escolher_opcao("\nEscolha a classe:", classes)


    pool = [15, 14, 13, 12, 10, 8]
    ordem = ["forca", "constituicao", "destreza", "inteligencia", "sabedoria", "carisma"]
    alocados = distribuir_atributos(pool, ordem)

    ficha = Ficha(
        nome=nome,        
        classe=classe,
        raca=raca,
        forca=alocados["forca"],
        atributo=0,
        constituicao=alocados["constituicao"],
        destreza=alocados["destreza"],
        inteligencia=alocados["inteligencia"],
        sabedoria=alocados["sabedoria"],
        carisma=alocados["carisma"],
    )

    print("\n=== Ficha Gerada ===")
    print(ficha)


    input("\nPressione Enter para rolar iniciativa...")
    print("Iniciativa:", ficha.iniciativa_rolar())

if __name__ == "__main__":
    main()
