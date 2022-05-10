## Importation des modules ##

import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi

## Définition des fonctions ##

def getData(filePath):
    '''
    Récupére les données envoyés par le Lidar (mettre un chemin absolu pour le chemin du fichier)
    '''

    x = np.array([])
    y = np.array([])

    with open(filePath, 'r') as fr:       #Ouvre le fichier texte
        linesTxt = fr.readlines()
        ptr = 1
        with open('./RPLIDAR2.txt','w') as fw:
            for lineTxt in linesTxt:                        # Enlève les 3 premieres lignes du fichier et rempli dans RPLIDAR2.txt
                if (ptr !=1 and ptr != 2 and ptr != 3):
                    l=lineTxt.split(' ')
                    x = np.append(x,l[0]) 
                    y = np.append(y,l[1])
                    fw.write(lineTxt)
                ptr += 1
            fw.close()
        fr.close()

    A = np.concatenate([[x], [y]], axis=0)

    return A


def changeBase(A):
    '''
    Passage des données en une base (distance, angle) en une base (x, y)
    '''
    X = np.array([])
    Y = np.array([])
    for (dist,angle) in zip(A[0,:],A[1,:]) :
        dist_i=float(dist)
        angle_i=float(angle)
        b1=angle_i*cos(dist_i*pi/180)/1000
        b2=angle_i*sin(dist_i*pi/180)/1000
        X=np.append(X, b1)
        Y=np.append(Y, b2)

    return X, Y


def createLines(X, Y):
    '''
    Crée les lignes à partir du nuage de point contenu dans X, Y et ne prend en compte que les lignes ayant au moins n points
    '''
    n = 2
    k = 0
    d = 0.01        # Rayon max dans lequel se trouvent 2 points d'une même ligne
    

    lines = np.empty((1, 2), int)
    coeffsDir = np.empty((1, 1), int)

    while(k<len(X)-1) :
        flag = True
        line = np.empty((1, 2), int)
        
    
        while(flag and k < len(X)-1) : 
                
            if((X[k+1] - X[k])**2 + (Y[k+1] - Y[k])**2 < d**2) :
                line = np.append(line, [[ X[k+1], Y[k+1] ]], axis=0)
                    
            else :
                flag = False
                
            k += 1
    
        if(len(line) > n+1) :
            
            line = np.delete(line, 0, axis=0)
            
            m = (line[-1, 1] - line[0, 1])/(line[-1, 0] - line[0, 0])
            coeffsDir = np.append(coeffsDir, [[m]], axis=0) 
            
                                
            lines = np.append(lines, [ line[0,:], line[-1,:] ], axis=0)         

    lines = np.delete(lines, 0, axis=0)
    return lines, coeffsDir
    

def reshapeLines(lines, coeffsDir, gamma):
    '''
    Relie les lignes si leur coeffs directeur et leur position sont similaire à gamma près
    '''
    linesReshape = np.empty((1, 2), int)
    coeffsDir = np.delete(coeffsDir, 0, axis=0)

    for i in range(0, len(lines) - 2, 2):

        linesReshape = np.append(linesReshape, [ lines[i,:] ], axis = 0)

        if(abs(coeffsDir[int(i/2)] - coeffsDir[int(i/2 + 1)]) < gamma
        and abs(lines[i, 0] - lines[i+2, 0]) < gamma
        and (lines[i, 1] - lines[i+2, 1]) < gamma):

            linesReshape = np.append(linesReshape, [ lines[i+2,:] ], axis = 0)

        else:

            linesReshape = np.append(linesReshape, [ lines[i+1,:] ], axis = 0)
                
                
    linesReshape = np.delete(linesReshape, 0, axis=0)
    print(np.size(linesReshape))
    return linesReshape



def printLines(lines):
    '''
    Affiche la carte sous forme de lignes
    '''

    for k in range(int(len(lines)/2)):
        print(k)
        print(lines[2*k, 0], lines[2*k+1, 0], lines[2*k, 1], lines[2*k+1, 1])
        plt.plot([ lines[2*i, 0], lines[2*i+1, 0] ], [ lines[2*i, 1], lines[2*i+1, 1] ])

    plt.draw()
    plt.show()
    


## Tests ##
'''
A = getData('Lidar_python/RPLIDAR.txt')

X, Y = changeBase(A)


lines  = createLines(X, Y, 5)[0]
coeffsDir = createLines(X, Y, 5)[1]
linesReshape = reshapeLines(lines, coeffsDir, 0.07)
'''