import numpy as np
import json

def AddValueToDict(k, d, v, i):
    # k = key - d = dict - v = value - i = type value
    # si le dictionnaire 'd' contient la clé 'k'
    # on récupère la valeur
    if k in d: i = d[k]
    # détermination du type de la valeur
    # si la valeur est de type set()
    if   isinstance(i, set):   i.add(v)
    # si la valeur est de type list()
    elif isinstance(i, list):  i.append(v)
    # si la valeur est de type str()
    elif isinstance(i, str):   i += str(v)
    # si la valeur est de type int()
    elif isinstance(i, int):   i += int(v)
    # si la valeur est de type float()
    elif isinstance(i, float): i += float(v)
    # on met à jour l'objet 'i' pour la clé 'k' dans le dictionnaire 'd'
    d[k] = i
    # on retourne le dictionnaire 'd'
    return d

def ConstructionJson (lines) :
    lines=np.array([[1,6], [3,6],[5,6],[7,6],[1,2],[3,4],[5,6],[7,8]])
    print(int(len(lines)/2))

    dictio = {}
    for i in range(0,int(len(lines)/2)):
        clef1="Mur"+str(i)+"PointFirst"
        clef2="Mur"+str(i)+"PointFinish"

        dictio=AddValueToDict(clef1, dictio, lines[2*i].tolist(), list())
        dictio=AddValueToDict(clef2, dictio, lines[2*i+1].tolist(), list())

    with open('RecupLigne.json', 'w') as mon_fichier:
        json.dump(dictio, mon_fichier)
