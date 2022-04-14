import numpy as np
from math import cos,sin,pi

#Code matlab
#function [Cx, Cy] = circle(Xc, Yc, R)
#    
#    theta = 0:0.01:2*pi;
#    Cx = Xc+R*cos(theta);
#    Cy = Yc+R*sin(theta);
#
#end

def circle(Xc,Yc,R):
    theta = np.linspace(0, 2*pi, 100)
    Cx =np.array([])
    Cy =np.array([])
    Cx = np.append(Cx,Xc+R*cos(theta)) 
    Cy = np.append(Cy,Yc+R*sin(theta)) 
    
    C =np.array([])
    C = np.concatenate([[Cx], [Cy]], axis=0)
    return C


