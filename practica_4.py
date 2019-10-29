lst=['M','X','Z','A']
lstN=[13,33,45,68]
lstD=[13,33,45,68,45,[1,2,3]]
# lst: ordenar en asc y desc.

# lstN: [13,4.5342,True,'hola mundo']

# lstD: eliminar los valores de la lista
# anidada uno a uno y agregar los siguientes # valores 4,5,6.
#[13,33,7,45,68,45,[4,5,6]]

# Anidar lst en lstN, anidar lstN en lstD,
# eliminar 'X' y agregar 'H' en lst.
# imprimir lst.

lst.sort()
lst.reverse()
print(lst)
lstN.pop(1)
lstN.pop(1)
lstN.pop(1)
lstN.append(4.5342)
lstN.append(True)
lstN.append('hola mundo')
print(lstN)
lstD[5].remove(1)
lstD[5].remove(2)
lstD[5].remove(3)
lstD[5].append(4)
lstD[5].append(5)
lstD[5].append(6)
print(lstD)
lstN.append(lst)
lstD.append(lstN)
lstD[6][4].remove('X')
lstD[6][4].append('H')
print(lstD)

#----------------------------------------------

# lstD: Imprimir en pantalla todos los
# valores, incluyendo los valores de
# listas anidadas.
dicin=[13, 33, 45, 68, 45, [4, 5, 6], [13, 4.5342, True, 'hola mundo', ['Z', 'M', 'A', 'H']]]
def lecturadic(lstD):
    for i in lstD:
        if type(i)==list:
            for ii in i:
                if type(ii)==list:
                    for iii in ii:
                        print(iii)
                else:
                    print(ii)
        else:
            print(i)
lecturadic(dicin)
#-----------------------------------------------