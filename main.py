from back_end import *


def main(self):

    ladino = Ficha(
        nome={self.nome}, atributo=0, classe={self.classe}, raca={self.raca},
        forca=10, constituicao=12, destreza=16, inteligencia=14, sabedoria=10, carisma=13
    )

    guerreiro = Ficha(
        nome={self.nome}, atributo=0, classe={self.classe}, raca={self.raca},
        forca=16, constituicao=15, destreza=12, inteligencia=10, sabedoria=12, carisma=8
    )

    barbaro = Ficha(
        nome={self.nome}, atributo=0, classe={self.classe}, raca={self.classe},
        forca=17, constituicao=16, destreza=12, inteligencia=8, sabedoria=10, carisma=10
    )


    print("=== Fichas ===")
    print(ladino, end="\n\n")
    print(guerreiro, end="\n\n")
    print(barbaro, end="\n\n")


    print("=== Iniciativas (d20 + DEX) ===")
    print(f"{ladino.nome}: {ladino.iniciativa_rolar()}")
    print(f"{guerreiro.nome}: {guerreiro.iniciativa_rolar()}")
    print(f"{barbaro.nome}: {barbaro.iniciativa_rolar()}")

    print("\n=== Rolagens de dano ===")
    print("Ladino (d8 + dex):", ladino.dado.d8())
    print("Guerreiro (d10 + for):", guerreiro.dado.d10())
    print("Bárbaro (d12 + for):", barbaro.dado.d12())

if __name__ == "__main__":
    main()
