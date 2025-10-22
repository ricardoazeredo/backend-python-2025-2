# class Carro:
#     def __init__(self, nome, cor):
#         self.nome = nome      # Atributo
#         self.cor = cor        # Atributo
#         self.velocidade = 0   # Atributo inicial

#     def acelerar(self):
#        self.velocidade += 10
#        print(f"{self.nome} está a {self.velocidade} km/h")

#     def frear(self):
#        self.velocidade -= 10
#        print(f"{self.nome} reduziu para {self.velocidade} km/h")

class Carro:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade +=10
        print(f"{self.nome} está a {self.velocidade} km/h")

    def frear(self):
        self.velocidade -= 10
        print(f"{self.nome} reduziu para {self.velocidade} km/h")    
        
carro1 = Carro("Fusca", "Azul") 
carro2 = Carro("Gol", "Vermelho") 
carro1.acelerar() 
carro2.acelerar() 
carro2.frear()
