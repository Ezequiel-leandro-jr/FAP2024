import time
import os

class Carro:
    def __init__(self, id, marca, modelo, ano):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def ligar_motor(self):
        print('Motor ligado!')      
    
    def info(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Ano: {self.ano}"

meu_carro = Carro('Toyota', 'Corolla', 2020)
meu_carro.ligar_motor
print(meu_carro.info())