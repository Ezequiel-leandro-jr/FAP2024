import time
import os

class Carro:
    def __init__(self, id, marca, modelo, ano):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def info(self):
        return 