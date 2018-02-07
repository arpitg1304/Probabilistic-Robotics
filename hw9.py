# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 00:28:09 2017

@author: Arpit
"""
import csv
from matplotlib import pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import math

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
onlyfiles = [f for f in listdir('LIDAR_360_degrees') if isfile(join('LIDAR_360_degrees', f))]

r = [];
stan_dev = [];
for i in range(0,36):
    file = onlyfiles[i]
    file_name = join(dir_path,'LIDAR_360_degrees',file)
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        integers = []
        for i in range(len(your_list)):
            string = ((your_list[i][0]))
            integers.append(int(string))
        r_temp = np.mean(integers)
        stan_temp = np.std(integers, ddof=1)
        r.append(r_temp)
        stan_dev.append(stan_temp)

r1 = np.sort(r)
r1 = r1.tolist()
Z = [x for _,x in sorted(zip(r,stan_dev))]

x = []
y = []
for i in range(len(r)):
    x.append( r[i] * math.cos(math.radians(10*i)))
    y.append( r[i] * math.sin(math.radians(10*i)))
    
plt.plot(r1,Z, 'g^')
plt.xlabel('mean')
plt.ylabel('standard deviation')
plt.show()
plt.plot(x,y, '--')
plt.show()