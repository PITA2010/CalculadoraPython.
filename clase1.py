import math

class OperacionAritmetica:
    operando1 = 0
    operando2 = 0

    def sumar(self):
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def dividir(self):
        return self.operando1 / self.operando2

    def multiplicar(self):
        return self.operando1 * self.operando2

class OperacionTrigonometrica:
    ang=0
    rad=0

    def seno (self):
        self.rad = math.radians(self.ang)
        return math.sin(self.rad)
    def coseno(self):
        self.rad = math.radians(self.ang)
        return math.cos(self.rad)
    def tangente (self):
        self.rad = math.radians(self.ang)
        return math.tan(self.rad)

class ConversionUnidades:
    num=0
    nume=0

    def CmM(self):
        self.nume= self.num/100
        return self.nume

    def Mcm(self):
        self.nume = self.num* 100
        return self.nume

    def gKg(self):
        self.nume = self.num / 1000
        return self.nume

    def Kgg(self):
        self.nume = self.num * 1000
        return self.nume

    def Fc(self):
        self.nume = (self.num * 0.5556) - 17.7778
        return self.nume

    def cF(self):
        self.nume=(self.num* 1.8) + 32
        return self.nume



