import numpy as np
from math import cos,sin,pi
import matplotlib.pyplot as plt

def circle(Xc,Yc,R):
    '''
    Fonction traçant des cercles centrés en Xc, Yc et de rayon R
    '''
    theta = np.linspace(0, 2*pi, 100)
    Cx = Xc + R*np.cos(theta)
    Cy = Yc + R*np.sin(theta)

    return Cx, Cy