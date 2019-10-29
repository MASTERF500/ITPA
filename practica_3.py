#1.Comentarios, Variables y Operadores
#2.Condicionales, Ciclos
"""
Contar del 1 al 100:
Inicio:
1
1.1,1.2,1.3,1.4… 1.9
2
2.1,2.2,2.3,2.4… 2.9
…
Intermedio:
50
50.1,50.2,50.3,50.4… 50.9
… 
99.1,99.2,99.3,99.4… 99.9
Final:
100
"""
#For
for i in range(1,101):
    if(i==1):
        print("Inicio: ")
    if(i==50):
        print("Intermedio: ")
    if(i==100):
        print("Final: ")
    print(i)
    for a in range(1,10):
        if(i!=100):
            print("{}.{}".format(i,a))
#While
cnt=0
while(cnt<100):
    cnt+=1
    if(cnt==1):
        print("Inicio: ")
    if(cnt==50):
        print("Intermedio: ")
    if(cnt==100):
        print("Final: ")
    print(cnt)
    for cnt2 in range(1,10):
        if(cnt!=100):
            print("{}.{}".format(cnt,cnt2))
        