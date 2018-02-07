# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Lidar and Ultrasound sensors data analysis and parameters when the signal is being reflected from a hard surface:\n")
import csv
import numpy as np
from matplotlib import pyplot as plt

"""
Reading data 
"""
with open('Midterm_F17_LIDAR_Ultrasound_100ms_1m_000.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

with open('Midterm_F17_LIDAR_Ultrasound_100ms_2m_000.csv', 'r') as f:
    reader = csv.reader(f)
    your_list1 = list(reader)
 
"""
Segregating the lists to Lidar and Ultrasound data
"""
"List of Lidar measurments from 1 meter"
integers1 = []
for i in range(len(your_list)):
    string = ((your_list[i][0]))
    integers1.append(int(string))

"List of Lidar measurments from 2 meter"
integers2 = []
for i in range(len(your_list1)):
    string = ((your_list1[i][0]))
    integers2.append(int(string))

"List of Ultrasound measurments from 1 meter"    
integers3 = []
for i in range(len(your_list)):
    string = ((your_list[i][1]))
    integers3.append(int(string))

"List of Ultrasound measurments from 2 meter"      
integers4 = []
for i in range(len(your_list1)):
    string = ((your_list1[i][1]))
    integers4.append(int(string))
    
plt.plot(integers1, '.')

plt.plot(integers2, '.')

"""
Finding mean and biases
"""
mean1 = np.mean(integers1)
mean2 = np.mean(integers2)

bias1 = mean1 - 100
bias2 = mean2 - 200
print("The bias in the measurment of the Lidar at 1 m is "+str(bias1))
print("The bias in the measurment of the Lidar at 2 m is "+str(bias2))

mean3 = np.mean(integers3)
mean4 = np.mean(integers4)

bias3 = (mean3 - 100)
bias4 = (mean4 - 200)
print("The bias in the measurment of the Ultrasound at 1 m is "+str(bias3))
print("The bias in the measurment of the Ultrasound at 2 m is "+str(bias4))

"""
Finding standard deviations
"""
std1 = np.std(integers1, ddof = 1)
std2 = np.std(integers2, ddof = 1)
print("The standard deviation of the measurment of the Lidar at 1 m is "+str(std1))
print("The standard deviation of the measurment of the Lidar at 2 m is "+str(std2))



std3 = np.std(integers3, ddof = 1)
std4 = np.std(integers4, ddof = 1)

print("The standard deviation of the measurment of the Ultrasound at 1 m is "+str(std3))
print("The standard deviation of the measurment of the Ultrasound at 2 m is "+str(std4))



"""
combining the measurements of the above measurments to produce the optimal estimate of the range and its standard deviation. 
"""
var1 = np.var(integers1, ddof = 1)
var2 = np.var(integers3, ddof =1)
w1_lidar = var2 / (float(var1 + var2))
w1_ultra = var1 / (float(var1 + var2))

"""
subtracting the biases from the measurments and multiplying with weights
"""
read1 = [i - bias1 for i in integers1]
read1 = [i * w1_lidar for i in read1]
read2 = [i - bias3 for i in integers3]
read2 = [i * w1_ultra for i in read2]

adjusted1 = [sum(x) for x in zip(read1, read2)]


var3 = np.var(integers2, ddof= 1)
var4 = np.var(integers4, ddof = 1)
w2_lidar = var4 / (float(var3 + var4))
w2_ultra = var3 / (float(var3 + var4))


read3 = [i - bias2 for i in integers2]
read3 = [i * w2_lidar for i in read3]
read4 = [i - bias4 for i in integers4]
read4 = [i * w2_ultra for i in read4]

adjusted2 = [sum(x) for x in zip(read3, read4)]

mean_adj1 = np.mean(adjusted1)
mean_adj2 = np.mean(adjusted2)
std_adj1 = np.std(adjusted1, ddof= 1)
std_adj2 = np.std(adjusted2, ddof = 1)

print("The mean of the sensors at 1 meter after adjustment is "+str(mean_adj1))
print("The mean of the sensors at 2 meter after adjustment is "+str(mean_adj2))

print("The standard deviation of the sensors at 1 meter after adjustment is "+str(std_adj1))
print("The standard deviation of the sensors at 2 meter after adjustment is "+str(std_adj2))