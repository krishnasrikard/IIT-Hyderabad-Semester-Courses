import numpy as np
import pandas as pd

data = pd.read_excel('input.xlsx')

df1 = data.loc[:,"Total" or "Marks"]

x = np.array(df1)

N = x.size                #Size of Data

x = x.reshape(N,1)
y =np.zeros((N,1))
 
X = np.hstack((x,y))    #Attach label column with data


k = 8           #No.of Clusters(Grades)

k_points = np.linspace(0,1,8)*np.max(x)       #Initialize clusters with some values
 
k_points = np.sort(k_points)
iterations = 50                    #No. of iterations

for iter in range(iterations):
    
    
    for i in range(N):              #Compute nearest cluster to a datapoint and 
                                    #attach its label to the datapoint.        
        dist = 999999
        
        for j in range(k):
            dist1 = (X[i][0]-k_points[j])**2
            if dist1<dist:
                X[i][1] = j + 1
                dist = dist1
    

    for i in range(k):       #Update cluster values by taking mean of corresponding labelled data
        
        s = 0
        c = 0
        for j in range(N):
            
            if X[j][1] == i+1:
                c += 1
                s += X[j][0]
        if c!=0:
            
            k_points[i] = s/c

grades = []

for i in range(N):              #Attach grades to the data points
    
    if X[i][1] == 1:
        grades.append('F')
    if X[i][1] == 2:
        grades.append('D')
    if X[i][1] == 3:
        grades.append('C-')
    if X[i][1] == 4:
        grades.append('C')
    if X[i][1] == 5:
        grades.append('B-')
    if X[i][1] == 6:
        grades.append('B')
    if X[i][1] == 7:
        grades.append('A-')
    if X[i][1] == 8:
        grades.append('A')

data['Grades'] = grades

data.to_excel('grades.xlsx',index = False)
