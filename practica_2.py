#Comentarios, Variables y Operadores
#Condicionales
"""
Entera: 40 <class 'int'>
Cadena A: Hola Mundo <class 'str'>
Cadena B: ! <class 'str'>
Real: 80.5 <class 'float'>

Entera + Real = [resulado] [tipo]
Cadena A + Cadena B = [resulado] [tipo]

Operadores en condicionales:
50<30: No es menor 
50>30: Si es mayor
50==30: No es igual
50!=30: Son diferentes
50>=30: Si es mayor ó igual
30<=50: Si es menor ó igual
"""

entero=40
cadena1='Hola Mundo'
cadena2='!'
real=80.5
r1="""
Entera: {0} {1}
Cadena1: {2} {3}
Cadena2 {4} {5}
Real: {6} {7}
""".format(entero,type(entero),cadena1,type(cadena1),cadena2,type(cadena2),real,type(real))
b1=entero+real
b2=cadena1+cadena2
r2="""
Entera + Real = {A} {B}
Cadena A + Cadena B = {C} {D}
""".format(A=b1,B=type(b1),C=b2,D=type(b2))
print(r1+r2)
print("Operadores en condicionales:")
v1=50
v2=30
if(v1<v2):
    print('{0}<{1}: No es menor'.format(v1,v2))
if(v1>v2):
    print('{0}>{1}: Si es mayor'.format(v1,v2))
if(v1==v2):
    print('{0}>{1}: No es igual'.format(v1,v2))
if(v1!=v2):
    print('{0}!={1}: Son diferentes '.format(v1,v2))
if(v1>=v2):
    print('{0}>={1}: Si es mayor ó igual '.format(v1,v2))
if(v2<=v1):
    print('{0}<={1}: Si es menor ó igual '.format(v2,v1))
#------------------------------------------
#Generar Ciclo While/For que imprima
#los números del 0 al 1000, mientras
#muestra un mensaje en pantalla para:
#No. 0: Inicio.
#No. 500: Intermedio.
#No. 1000: Final.

#For
num=range(1,1001)
for i in num:
    if(i==1):
        print("No. {}: Inicio".format(i))
    if(i==500):
        print("No. {}: Intermedio".format(i))
    if(i==1000):
        print("No. {}: Final".format(i))
    #print(i)
#while
num1=0
while(num1<1000):
    num1+=1
    if(num1==1):
        print("No. {}: Inicio".format(num1))
    if(num1==500):
        print("No. {}: Intermedio".format(num1))
    if(num1==1000):
        print("No. {}: Final".format(num1))
    #print(num1)
