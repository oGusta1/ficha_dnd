import random

class Dados:
    def __init__(self):
        self._rng = random

    def rolar(self, faces: int) -> int:
        return self._rng.randint(1, faces)

    def d4(self) -> int:  return self.rolar(4)
    def d6(self) -> int:  return self.rolar(6)
    def d8(self) -> int:  return self.rolar(8)
    def d10(self) -> int: return self.rolar(10)
    def d12(self) -> int: return self.rolar(12)
    def d20(self) -> int: return self.rolar(20)


class Atributo:
    def __init__(self, ponto_atributo: int = 10):
        self.ponto_atributo: int = int(ponto_atributo)
        self.modificador: int = self.calcular_modificador()

    def calcular_modificador(self) -> int:
        mod = (self.ponto_atributo - 10) // 2
        self.modificador = mod
        return mod


class Ficha:
    vida_regras = {
        "Ladino":    {"dado": 8,  "min": 5},
        "Guerreiro": {"dado": 10, "min": 6},
        "Bárbaro":   {"dado": 12, "min": 7},
    }

    def __init__(self, nome, atributo, classe, raca,
                 forca, constituicao, destreza, inteligencia, sabedoria, carisma):
        self.nome = nome
        self.atributo = atributo
        self.classe = classe
        self.raca = raca

  
        self.forca = Atributo(forca)
        self.constituicao = Atributo(constituicao)
        self.destreza = Atributo(destreza)
        self.inteligencia = Atributo(inteligencia)
        self.sabedoria = Atributo(sabedoria)
        self.carisma = Atributo(carisma)

        self.dado = Dados()


        self.vida = self.calculo_vida()
        self.ca = self.ca_ficha()

        self.iniciativa = 0

    def calculo_vida(self) -> int:
        regra = self.vida_regras.get(self.classe)
        if not regra:
            raise ValueError(f"Classe sem regra de vida: {self.classe}")
        faces = regra["dado"]
        minimo = regra["min"]
        roll = self.dado.rolar(faces)
        base = max(roll, minimo)
        return max(base + self.constituicao.modificador, 1)

    def ca_ficha(self) -> int:
        return 10 + self.destreza.modificador

    def iniciativa_rolar(self) -> int:
        self.iniciativa = self.dado.d20() + self.destreza.modificador
        return self.iniciativa

    def resumo(self) -> dict:
        return {
            "nome": self.nome,
            "raca": self.raca,
            "classe": self.classe,
            "vida": self.vida,
            "ca": self.ca,
            "forca": {"pontos": self.forca.ponto_atributo, "mod": self.forca.modificador},
            "destreza": {"pontos": self.destreza.ponto_atributo, "mod": self.destreza.modificador},
            "constituicao": {"pontos": self.constituicao.ponto_atributo, "mod": self.constituicao.modificador},
            "inteligencia": {"pontos": self.inteligencia.ponto_atributo, "mod": self.inteligencia.modificador},
            "sabedoria": {"pontos": self.sabedoria.ponto_atributo, "mod": self.sabedoria.modificador},
            "carisma": {"pontos": self.carisma.ponto_atributo, "mod": self.carisma.modificador},
        }

    def __str__(self) -> str:
        r = self.resumo()
        return (
            f"Nome: {r['nome']} | Raça: {r['raca']} | Classe: {r['classe']}\n"
            f"Vida: {r['vida']} | CA: {r['ca']}\n"
            f"Força {r['forca']['pontos']} (mod {r['forca']['mod']}) | "
            f"Destreza {r['destreza']['pontos']} (mod {r['destreza']['mod']})\n"
            f"Constituição {r['constituicao']['pontos']} (mod {r['constituicao']['mod']}) | "
            f"Inteligência {r['inteligencia']['pontos']} (mod {r['inteligencia']['mod']})\n"
            f"Sabedoria {r['sabedoria']['pontos']} (mod {r['sabedoria']['mod']}) | "
            f"Carisma {r['carisma']['pontos']} (mod {r['carisma']['mod']})"
        )
