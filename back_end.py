import random

class Dados:
    
    d4 : int
    d6 : int
    d8 : int
    d10 : int
    d12 : int 
    d20 : int
    
    def d4():
        return random.randint(1,4)

    def d6():
        return random.randint(1,6)
    
    def d8():
        return random.randint(1,8)
    
    def d10():
        return random.randint(1,10)
    
    def d12():
        return random.randint(1,12)
    
    def d20():
        return random.randint(1,20)
    
class Ficha_dnd:
    nome : str
    atributo : int
    classe : str 
    raca : str 
    vida : int
    ca : int
    iniciativa : int
    
    def __init__(self, nome, atributo, classe, raca, ability, vida, ca,iniciativa):
        self.nome = nome
        self.atributo = atributo
        self.classe = classe
        self.raca = raca
        self.ability = ability
        self.vida = vida
        self.ca = ca
        self.iniciativa = iniciativa


class Atributos:
    
    forca : 0
    destreza : 0
    constituicao : 0
    inteligencia : 0
    sabedoria : 0
    carisma : 0



    
    