# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:32:18 2017

@author: raghav
"""

import numpy as np
from random import *

from k_means_implementation import *

f = open('output.txt','w')

#For Calculations
loop_run = 0

best_purity_score = 0

#To find the best centroid list and purity value
best_centroids = np.array([0]*cluster_count)
best_purity_score = 0

#Initializing number of trails
purity_run = randint(10,20)

#Running the k means algorithm defined in assignment1problem1.py
#To compute purity score
while (loop_run < purity_run):
    
    f.write("\n"+"Iteration"+" "+str(loop_run)+"\n")
    print("\n","Iteration",loop_run)
    #Function call - To get upadted and final centroid and cluster asssignments
    value,centroids = kmeans()
    
    #Initialising confession matrix - To count instances of individual class labels
    confusion_matrix = np.zeros((cluster_count, cluster_count))
    
    iteration_variable = 0
    
    #Computing confession matrix
    for j in value:
        confusion_matrix[iteration_variable][0] = sum((items > 0) & (items <= 50) for items in j)
        confusion_matrix[iteration_variable][1] = sum((items > 50) & (items <= 100) for items in j)
        confusion_matrix[iteration_variable][2] = sum((items > 100) & (items <= 150) for items in j)
        iteration_variable += 1
    
    f.write("\n Confusion_matrix \n")
    f.write(str(confusion_matrix))
    #Intermediate step while calculating purity
    #Weighted sum - Summing the maximum instances represented from every label 
    cluster_sum = sum(max(i) for i in confusion_matrix)
    
    #Calculating purity score respective to this centroid initialisation
    purity_score = cluster_sum/len(data)

    
    #Finding the best purity value and the respective centroid points found among the different trails
    if(purity_score >= best_purity_score):
        best_purity_score = purity_score
        best_centroid_points = np.copy(centroids)
        

    f.write("\n Found Purity score"+"\n")
    f.write(str(purity_score)+"\n")
    f.write("Best purity score"+"\n")
    f.write(str(best_purity_score)+"\n")
    f.write("Corresponding centroid points"+"\n")
    f.write(str([l.tolist() for l in centroid_points])+"\n")
    
    loop_run += 1

print("Purity Score")
print(best_purity_score)
f.write("\n \n"+"Best Purity Score"+" "+str(best_purity_score))
print("Respective centroid points making the best purity score")
print(best_centroid_points)
f.write("\n"+"Respective Centroid points"+"\n"+str(best_centroid_points))
f.close()

    
    