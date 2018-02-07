
# coding: utf-8

# In[3]:

import numpy as np
import matplotlib.pyplot as plt
import csv
import math

#current state
predict_state = np.matrix([[2530],[-10]])

R_mat = np.matrix([[0.1,1],[1,10]])

#Q matrix is given
Q = np.matrix([10])

#Covariance of position and velocity
Covariance = np.matrix([[100,0],[0,100]])

#Control input matrix
A = np.matrix([[1,0.1],[0,1]])

#covariance of noise
C=np.matrix([1,0])

Identity = np.matrix([[1,0],[0,1]])

data = []

#Reading data from file
with open ('RBE500-F17-100ms-Constant-Vel.csv','r') as csvfile:
    data_points = csv.reader(csvfile)
    read_list = list(data_points)

for i in read_list:
    data.append(int(i[0]))

time = []
position_list = []
velocity_list = []
position_sd = []
velocity_sd = []
correlation_coeff = []

#Prediction and update steps
for i in range(0,300):
    
    expected_innovation = C * Covariance * C.T + Q
    
    predict_state_init = A*predict_state
    
    Covariance_init = (A)*(Covariance)*(A.T) + R_mat

    S = C*Covariance_init*C.T + Q

    Kalman_gain = Covariance_init* C.T * S.I

    V = data[i]- C * predict_state_init   
    
    d = V*V/expected_innovation
    
    if d>= 9:
        
        predict_state = predict_state_init
        
        Covariance = Covariance_init
        
        position_list.append(predict_state_init[0,0]) 
        
        velocity_list.append(predict_state_init[1,0])
        
        position_sd.append(math.sqrt(Covariance_init[0,0]))
        
        velocity_sd.append(math.sqrt(Covariance_init[1,1]))
        
    if d<9:
        
        predict_state = predict_state_init + Kalman_gain * V
            
        Covariance  = (Identity-(Kalman_gain*C))*Covariance_init
        
        position_list.append(predict_state[0,0]) 
        
        velocity_list.append(predict_state[1,0])
        
        position_sd.append(math.sqrt(Covariance[0,0]))
        
        velocity_sd.append(math.sqrt(Covariance[1,1]))
        
       
    time.append(i)

    
    correlation_coeff.append(Covariance[0,1]/(math.sqrt(Covariance[0,0]) * math.sqrt(Covariance[1,1])))

#Plotting of all the graphs
plt.plot(time, position_list, data, '-')
plt.xlabel('Time (s)')
plt.ylabel('Positions(cm)')
plt.title('Estimated positions and real positions')
plt.show()
plt.plot(time,velocity_list, 'r-')
plt.xlabel('Time (s)')
plt.ylabel('Velocty (cm/s)')
plt.title('Velocity Estimation')
plt.show()
plt.plot(time,position_sd, velocity_sd, 'b-')
plt.xlabel('Time (s)')
plt.ylabel('Standard deviations')
plt.title('Standard deviation')
plt.show()
plt.plot(time, correlation_coeff, 'y-')
plt.xlabel('Time (s)')
plt.ylabel('Correlation Coefficient')
plt.title('Correlation Coefficient')
plt.show()

