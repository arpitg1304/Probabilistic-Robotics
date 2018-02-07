# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 22:41:59 2017

@author: Arpit
"""
import csv
import numpy as np


"""
reading CSV file and saving it in a list: your_list
"""
with open('LIDAR_100ms_Wander.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

"""
Convert list of lists to list of integers
"""    
integers = []
for i in range(len(your_list)):
    string = ((your_list[i][0]))
    integers.append(int(string))

"""
Making time stamp list
"""
time_stamp = [0]
for i in range(1,len(integers)):
    time_stamp.append(i/100)
    
"""
Readings suspiciously out of range and suspiciously minimum measurments
"""
abovemax = []
below_min = []
wall_region = []
actual_range = []
for i in range(len(integers)):
    if integers[i] > 4000:
        abovemax.append(integers[i])
    if integers[i] < 5:
        below_min.append(integers[i])
    if integers[i] >= 3000 and integers[i] <= 3500:
        wall_region.append(integers[i])
    if integers[i] > 5 and integers[i] < 3000:
        actual_range.append(integers[i])
 
"""
Finding probabilities of suspiciously out of range and minimum measurments
"""       
prob_out = len(abovemax) / len(integers)
print("Probability of obtaining a suspiciously out of range measurement is "+str(prob_out))
prob_min = len(below_min) / len(integers)
print("Probability of obtaining a suspiciously minimum measurment is "+str(prob_min))

mean_wall_region = sum(wall_region) /len(wall_region)
print("Mean of actual wall range measurment is "+str(mean_wall_region))

std_wall_region = np.std(wall_region)
print("Standard deviation of actual wall range measurment is "+str(std_wall_region))

"""
Finding number of objects
"""
def velo(a):
    for i in range(a,len(integers)):
        if abs(integers[i] - integers[i+1]) >100:
            break
        velocity = abs(integers[i] - integers[i+1])/10
        vel.append(velocity)
        
count = 0
vel = []
for i in range(1,len(integers)):
    if abs(integers[i] - integers[i-1]) >1000 and integers[i]>5 and integers[i]<3000:
        count = count +1
        velo(i)
print("Number of objects detected are "+str(count))
print("Maximum velocity of an object is "+str(np.max(vel))+ "m/s")

"""
probability that a given measurement is an object and not the wall 
"""
prob = len(actual_range) / (len(actual_range) + len(wall_region))

print("probability - given measurement is an object and not the wall is "+str(prob))

"""
STarting EM Algorithm
"""

def em(models):
    sigma = 2.0
    lambda = 0.01
    mean = mean_wall_region
    c = [0.2, 0.2, 0.2, 0.2, 0.2]
    



