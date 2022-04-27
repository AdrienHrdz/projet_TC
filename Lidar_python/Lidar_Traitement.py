## Importation des modules ##

import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi
import circle as circle


## Définition des fonctions ##

def getData(filePath):
    '''
    Récupére les données envoyés par le Lidar
    '''

    x = np.array([])
    y = np.array([])

    with open(filePath, 'r') as fr:       #Ouvre le fichier texte
        linesTxt = fr.readlines()
        ptr = 1
        with open('Lidar_python/RPLIDAR2.txt','w') as fw:
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
    #A = getData()
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
    Crée les lignes à partir du nuage de point contenu dans X, Y
    '''
    #X = changeBase()[0]
    #Y = changeBase()[1]

    k = 0
    d = 0.01        # Rayon max dans lequel se trouvent 2 points d'une même ligne
    n = 5           # Nbs de points minimum dans une ligne

    lines = np.empty((1, 2), int)
    coeffsDir = np.empty((1, 1), int)

    while(k<len(X)-1) :
        flag = True
        line = np.empty((1, 2), int)
        
    
        while(flag and k < len(X)-1) : 
            #(Cx, Cy) = circle.circle(X[k], Y[k], d)
                
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

    return lines


#% for i = 2:2:len(lines)
#%     for j = 2:2:len(lines)
#%        if(i ~= j && abs(coeffsDir(i/2) - coeffsDir(j/2)) < gamma ...
#%                && abs(lines(i, 1) - lines(j, 1)) < gamma && abs(lines(i, 2) - lines(j, 2)) < gamma)
#%            lines(i,:) = []; 
#%            lines(i+1,:) = [];
#% 
#%        else
#%        end
#%     end
#%    
#% end
#


def printLines(lines):
    '''
    Affiche la carte sous forme de lignes
    '''
    lines = np.delete(lines, 0, axis=0)

    for i in range(int(len(lines)/2)):
        plt.plot([ lines[2*i, 0], lines[2*i+1, 0] ], [ lines[2*i, 1], lines[2*i+1, 1] ])

    plt.draw()


## Tests ##
A = getData('Lidar_python/RPLIDAR.txt')

X = changeBase(A)[0]
Y = changeBase(A)[1]

lines = createLines(X, Y)

printLines(lines)
