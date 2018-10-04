from clase1 import *

print("Digita \n"
      "1 para sumar, \n"
      "2 para restar, \n"
      "3 para multiplicar, \n"
      "4 para dividir,\n"
      "5 para realizar la funcion seno, \n"
      "6 para realizar la funcion coseno, \n"
      "7 para realizar la funcion tangente, \n"
      "8 para convertir de centimetros a metros, \n"
      "9 para convertir metros a centimetros\n"
      "10 para convertir de gramos a Kilogramos\n"
      "11 para convertir de Kilogramos a gramos\n"
      "12 para convertir de Fahrenheit a Celsius\n"
      "13 para convertir de Celsius a Fahrenheit\n")




miCalculadoraA=OperacionAritmetica()
miCalculadoraT=OperacionTrigonometrica()
miCalculadoraC=ConversionUnidades()
x=int(input())

if x==1:
    print("Ingrese el primer numero")
    miCalculadoraA.operando1 = int(input())
    print("Ingrese el segundo numero")
    miCalculadoraA.operando2 = int(input())
    print("la suma es", miCalculadoraA.sumar())
    SystemExit

if x==2:
    print("Ingrese el primer numero")
    miCalculadoraA.operando1 = int(input())
    print("Ingrese el segundo numero")
    miCalculadoraA.operando2 = int(input())
    print("la resta es", miCalculadoraA.restar())

if x==3:
    print("Ingrese el primer numero")
    miCalculadoraA.operando1 = int(input())
    print("Ingrese el segundo numero")
    miCalculadoraA.operando2 = int(input())
    print("la multiplicacion es", miCalculadoraA.multiplicar())

if x==4:
    print("Ingrese el primer numero")
    miCalculadoraA.operando1 = int(input())
    print("Ingrese el segundo numero")
    miCalculadoraA.operando2 = int(input())
    print("la division es", miCalculadoraA.dividir())

if x==5:
    print("Ingrese el angulo")
    miCalculadoraT.ang = int(input())
    print("el seno del angulo es", miCalculadoraT.seno())

if x==6:
    print("Ingrese el angulo")
    miCalculadoraT.ang = int(input())
    print("el coseno del angulo es", miCalculadoraT.coseno())

if x==7:
    print("Ingrese el angulo")
    miCalculadoraT.ang = int(input())
    print("la tangente del angulo es", miCalculadoraT.tangente())

if x==8:
    print("Ingrese la cantidad a convertir")
    miCalculadoraC.num = int(input())
    print(miCalculadoraC.num,"centimetros, equivalen a ", miCalculadoraC.CmM(),"metros")

if x==9:
    print("Ingrese la cantidad a convertir")
    miCalculadoraC.num = int(input())
    print(miCalculadoraC.num,"metros, equivalen a ", miCalculadoraC.Mcm(),"centimetros")

if x==10:
    print("Ingrese la cantidad a convertir")
    miCalculadoraC.num = int(input())
    print(miCalculadoraC.num,"gramos, equivalen a ", miCalculadoraC.gKg(),"Kilogramos")

if x==11:
    print("Ingrese la cantidad a convertir")
    miCalculadoraC.num = int(input())
    print(miCalculadoraC.num,"Kilogramos, equivalen a ", miCalculadoraC.Kgg(),"gramos")

if x==12:
    print("Ingrese la cantidad a convertir")
    miCalculadoraC.num = int(input())
    print(miCalculadoraC.num,"°F, equivalen a ", miCalculadoraC.Fc(),"°C")

if x==13:
    print("Ingrese la cantidad a convertir")
    miCalculadoraC.num = int(input())
    print(miCalculadoraC.num,"°C, equivalen a ", miCalculadoraC.cF(),"°F")


