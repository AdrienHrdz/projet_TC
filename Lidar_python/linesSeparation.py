import numpy as np
from math import cos,sin,pi
import matplotlib.pyplot as plt

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
    Cx = Xc + R*np.cos(theta)
    Cy = Yc + R*np.sin(theta)
   
    return Cx, Cy


