from multiprocessing.connection import wait
import sys
import numpy as np
from rplidar import RPLidar,RPLidarException
import matplotlib.pyplot as plt
from math import cos,sin,pi
from Lidar_Traitement import getData, changeBase, createLines, printLines
PORT_NAME = 'COM11'


def analyse(lidar):
    for i, scan in enumerate(lidar.iter_scans('express')):
        data.append([[scan[j][1] for j in range(len(scan))],[scan[j][2] for j in range(len(scan))]])
        Angle = data[i][0]
        Distance = data[i][1]

        x=np.array(Angle)
        y=np.array(Distance)
        A = np.concatenate([[x], [y]], axis=0)
        X = changeBase(A)[0]
        Y = changeBase(A)[1]
        lines = createLines(X, Y)
        printLines(lines)

        plt.pause(0.5)
        plt.close()

        if i == 100:
           break

lidar = RPLidar(PORT_NAME)
data = []

try:
    analyse(lidar)
except ValueError:
    print('Issue : Value Error')
    analyse(lidar)
except RPLidarException:
    print('Issue : RPlidar Error')
    analyse(lidar)

