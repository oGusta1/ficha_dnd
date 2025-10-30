import random

class Dados:
    def __init__(self):
        self._rng = random
    
    def d4(self) -> int:
        return self._rng.randint(1,4)

    def d6(self) -> int:
        return self._rng.randint(1,6)
    
    def d8(self) -> int:
        return self._rng.randint(1,8)
    
    def d10(self) -> int:
        return self._rng.randint(1,10)
    
    def d12(self) -> int:
        return self._rng.randint(1,12)
    
    def d20(self) -> int:
        return self._rng.randint(1,20)
    
class Atributo:
    
    def __init__(self, ponto_atributo: int = 0):
        self.ponto_atributo: int = int(ponto_atributo)
        self.modificador: int = self.calcular_modificador()

    def calcular_modificador(self) -> int:
        mod = (self.ponto_atributo - 10) // 2
        self.modificador = mod
        return mod
   
class Ficha:
    nome : str
    atributo : int
    classe : str 
    raca : str 
    vida : int
    ca : int
    iniciativa : int

    vida_regras = {
    "Ladino": {"dado": 8, "min": 5},
    "Guerreiro":{"dado": 10, "min": 6},
    "Bárbaro": {"dado": 12, "min": 7},
}

    def __init__(self, nome, atributo, classe, raca, forca, constituicao, destreza, inteligencia, sabedoria, carisma):
        self.nome = nome
        self.atributo = atributo
        self.classe = classe
        self.raca = raca
        self.vida = self.ca_vida()
        self.ca = self.calculo_vida
        self.iniciativa = 0

        self.forca: Atributo = Atributo(forca)
        self.constituicao: Atributo = Atributo(constituicao)
        self.destreza: Atributo = Atributo(destreza)
        self.inteligencia: Atributo = Atributo(inteligencia)
        self.sabedoria: Atributo = Atributo(sabedoria)
        self.carisma: Atributo = Atributo(carisma)

        self.dado = Dados()

    def calculo_vida(self):
        regra = self.vida_regras.get(self.classe)
        
        faces = regra["dado"]
        minimo = regra ["min"]

        roll = self.dado.rolar(faces)
        base = max(roll, minimo)
        self.vida = max(base + self.constituicao.modificador,1)

        return
    
    def ca_ficha(self) -> int:

        return 10 + self.destreza.modificador

    def iniciativa(self) -> int:
        rolagem = self.dado.d20()
        mod_dex = self.destreza.modificador
        return rolagem + mod_dex
    

    def __str__(self) -> str:
        return {
            "nome": self.nome,
            "raca": self.raca,
            "classe": self.classe,
            "forca":{"pontos de forca":self.forca.ponto_atributo, "mod": self.forca.modificador},
            "destreza":{"pontos de destreza": self.destreza.ponto_atributo, "mod": self.destreza.modificador},
            "constituicao":{"pontos de constituicao": self.constituicao.ponto_atributo, "mod": self.constituicao.modificador},
            "inteligencia":{"pontos de inteligencia": self.inteligencia.ponto_atributo, "mod": self.inteligencia.modificador},
            "sabedoria": {"pontos de sabedoria": self.sabedoria.ponto_atributo, "mod": self.sabedoria.modificador},
            "carisma": {"pontos de carisma": self.carisma.ponto_atributo, "mod": self.carisma.modificador},
        }



    
    