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
    
    #print(int(len(lines)/2))
    dictio = {}
    for i in range(0,int(len(lines)/2)):
        dicky ={}

        clef0=str(i)
        clef1="First"
        clef2="Finish"
        
        dicky=AddValueToDict(clef1, dicky, lines[2*i].tolist(), list())
        dicky=AddValueToDict(clef2, dicky, lines[2*i+1].tolist(), list())
        dictio=AddValueToDict(clef0, dictio, dicky, list())


    with open('RecupLigne.json', 'w') as mon_fichier:
        json.dump(dictio, mon_fichier)

lines=np.array([[ 0.11283354, 0.04369888],
 [ 0.10184537  , 0.1813602 ],
 [ 0.07624975 , 0.22122833],
 [ 0.01508276  ,0.22248935],
 [ 0.00498009  ,0.11989662],
 [-0.01715755  ,0.11977737],
 [-0.06576925  ,0.22248237],
 [-0.0933768   ,0.22758904],
 [-0.0990632  , 0.22735541],
 [-0.13549654 , 0.23238263],
 [-0.14552383 , 0.19084762],
 [-0.14382285 , 0.034914  ],
 [-0.14613511 ,-0.01592258],
 [-0.15041535 ,-0.10597746],
 [-0.1250683  ,-0.11366143],
 [ 0.09079997 ,-0.12314368],
 [ 0.08876227 ,-0.09634449],
 [ 0.10063716 ,-0.06536178]])

#lines=np.array([[1,6], [3,6],[5,6],[7,6],[1,6], [3,6],[5,6],[7,6]])
ConstructionJson(lines)