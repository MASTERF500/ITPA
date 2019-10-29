"""
Resultado: 
Curso de Python:
Comentarios, Variables y Operadores.
Variables
Entera: 3389 <class 'int'>
Cadena: Hola Mundo <class 'str'>
Real: 3.1416 <class 'float'>
Booleana: True <class 'bool'>

Operadores:
50x30= 1500
50/30= 1.66
50-30= 20
50+30= 80
5**30= 125

R= A:1500, B:1.66, C:20, D:80 y E:125

Fin de Hola Mundo!
"""
#----------------------------------------
a1=3389
a2='Hola Mundo'
a3=3.1416
a4=True
r1="""
Resultado: 
Curso de Python:
Comentarios, Variables y Operadores.
Variables
Entera: {0} {1}
Cadena: {2} {3}
Real: {4} {5}
Booleana: {6} {7}
""".format(a1,type(a1),a2,type(a2),a3,type(a3),a4,type(a4))
b1=50*30
b2=50/30
b3=50-30
b4=50+30
b5=5**3
r2="""
Operadores:
50x30= {A} 
50/30= {B}
50-30= {C}
50+30= {D}
5**3= {E}
R= A:{A}, B:{B}, C:{C}, D:{D} y {E}:125
""".format(A=b1,B=b2,C=b3,D=b4,E=b5)
print(r1+r2)
