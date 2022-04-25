import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi
import circle as circle

# Variables globales
sigma = 0.01 # Largeur d'une ligne
d = 0.01 # Rayon max dans lequel se trouvent 2 points d'une même ligne
n = 10 # Nbs de points minimum dans une ligne
gamma = 0.4 # Difference accepté pour regrouper 2 lignes

# Récupération des données

#[A,count]=fscanf(fid,'%g%g%g',[3 inf]); %sépare les données en 3 colonnes
#A(3,:)=[];%supprime la ligne qualité

x=np.array([])
y=np.array([])
#A.append(x[1]) B.append(x[2])
with open('Lidar_python/RPLIDAR.txt','r') as fr: #Ouvre le fichier texte
    lines = fr.readlines()
    ptr = 1
    with open('RPLIDAR2.txt','w') as fw:
        for line in lines: #enlève les 3 premieres lignes du fichier et rempli dans RPLIDAR2.txt
            if (ptr !=1 and ptr != 2 and ptr != 3):
                l=line.split(' ')
                x=np.append(x,l[0]) 
                y=np.append(y,l[1])
                fw.write(line)
            ptr += 1
        fw.close()
    fr.close()
A=np.concatenate([[x], [y]], axis=0)
#Matrice ligne 1 : angle / ligne 2 : distance

# Changement de bases

#X=A(2,:).*cos(A(1,:).*(pi/180))./1000;
#Y=A(2,:).*sin(A(1,:).*(pi/180))./1000;

X=np.array([])
Y=np.array([])
for (dist,angle) in zip(A[0,:],A[1,:]) :
    dist_i=float(dist)
    angle_i=float(angle)
    b1=angle_i*cos(dist_i*pi/180)/1000
    b2=angle_i*sin(dist_i*pi/180)/1000
    X=np.append(X,b1)
    Y=np.append(Y,b2)

#points = np.concatenate([[X], [Y]], axis=0)

#Traçage de lignes
k = 1
lines = np.array([])
coeffsDir = np.array([])

while(k<len(X)-1) :
    flag = True
    line = np.array([0, 0])
   
    while(flag and k < len(X)-1) : 
        (Cx, Cy) = circle.circle(X[k], Y[k], d)
        plt.plot(Cx, Cy)
            
        if((X[k+1] - X[k])**2 + (Y[k+1] - Y[k])**2 < d**2) :
            line = np.concatenate((line, [ X[k+1], Y[k+1] ]), axis=0)
            print(line, "\n", line.shape)
            
                
        else :
            flag = False
            
        k += 1
  
    if(len(line) > n) :
       m = (line[-1, 1] - line[0, 1])/(line[-1, 0] - line[0, 0])
       coeffsDir = np.concatenate((coeffsDir, m));                            
       
       lines = np.concatenate(( lines, [line[0,:], line[-1,:]] )); 



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
#Affichage
#for i = 0:len(lines)/2 - 1
#    plot(lines(1+2*i:2*(i+1),1), lines(1+2*i:2*(i+1), 2)); hold on;
#   
#end
#
#status=fclose(fid); #ferme fichier
