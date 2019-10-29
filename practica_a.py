a=33293
b='Hola Mundo'
c=3.1416
d=False
cadena1='''
Variables:
Entera: {} {}
Cadena: {} {}
Real: {} {}
Booleana: {} {}
'''.format(a,type(a),b,type(b),c,type(c),d,type(d))
x=50
y=30
mult=x*y
div=x/y
sum2=x+y
rest=x-y
cadena2='''
Operadores:
{A}x{B}={C}
{A}/{B}={D}
{A}+{B}={E}
{A}-{B}={F}
5**3={I}
'''.format(A=x,B=y,C=mult,D=div,E=sum2,F=rest,I=5**3)

cadena3='\nRM={},RD={},RS={},RR={},RE={}'.format(mult,div,sum2,rest,5**3)
print(cadena1+cadena2+cadena3)