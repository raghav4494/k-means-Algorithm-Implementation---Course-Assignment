# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:53:30 2017

@author: raghav
"""
import numpy as np
import random
import sys
import math

#Reading source data
data = np.genfromtxt('iris.txt',dtype=None,delimiter=",",usecols=(0,1,2,3))
#data = np.genfromtxt('data.txt',dtype=None,delimiter=",",usecols=(0))

#defining k clusters
cluster_count = int(sys.argv[1])

#Question 1a
print("1a) Number of data points in the file")
print(len(data))

#Question 1b
print("1b) Dimensions of dataset")
try:
    no_of_rows = data.shape[0]
    no_of_cols = data.shape[1]
except IndexError:
    no_of_rows = 1
    no_of_cols = data.shape[0]
print(no_of_rows,"*",no_of_cols)


#Question 1c
print("1c) Number of clusters")
print(cluster_count)

#Mathematical function to find distance between any two points
def finding_distance(x,y):
    distance = 0
    loop = 0
    #Considering both 1D and nD data points and centroids
    try:
        while(loop < no_of_cols):
            distance += ((x[loop]-y[loop])**2)
            loop+=1
    except IndexError:
        #For 1D data
        while(loop < no_of_cols):
            distance = ((float(x)-float(y))**2)
            loop+=1
        
    return math.sqrt(distance)

#Computing SSE - sum of squared error
def sse_calculation(x,y):
    total = 0
    index = 0
    cluster_iterator = 0
    try:
        while(cluster_iterator < cluster_count):
            loop_variable=0
            while(loop_variable < no_of_cols):
                total += ((x[cluster_iterator][loop_variable]-y[cluster_iterator][loop_variable])**2)
                loop_variable += 1
            cluster_iterator += 1
    except IndexError:
        #For 1D data
        x1 = float(x[index])
        y1 = float(y[index])
        while(index < no_of_cols):
            sub = (x1-y1)
            total += (sub * sub)
            index += 1    
        
    return math.sqrt(total)


# Implementation of k-means algorithm
def kmeans():
        
    #initialising initial centroids
    centroids = random.sample(list(data),cluster_count)
    print("Initial Seeds")
    print([l.tolist() for l in centroids])
    
    #defining epsilon - to check for convergence
    epsilon = 0.001
    
    #For calculation purpose
    convergence_variable = 10
    distances = [0] * cluster_count
    minimum_index = 0
    
    #To find the number of iterations it took to converge
    iteration_count = 0
    
    #To keep track of previous centroid list
    #old_centroids = [0]*cluster_count
    
    while (convergence_variable >5):
        count = 0
    
        #Initialisation of clusters - based on given k value
        clusters = [[] for _ in range(cluster_count)]
        
        #To find the ids of the points fitting each cluster
        ids = [[] for _ in range(cluster_count)]
               
        #Cluster Assignment
        while (count < len(data)):
            #For calculation purpose
            loop_count = 0
                       
            #Computing distance of every point from the given centroids
            while loop_count < cluster_count:
                distances[loop_count] = finding_distance(data[count],centroids[loop_count])
                loop_count+=1
            
            #Finding the cluster where the point fits
            minimum_index = distances.index(min(distances))
            
            #Appending values to respective clusters
            clusters[minimum_index].append(data[count])
            
            #To match the line number in dataset and cluster assignment 
            #Adding 1 - Since We assume id of first point in data set is 1.
            ids[minimum_index].append(count+1)
            count+=1
        
        count = 0

        #Copying old centroids before updating centroids
        old_centroids = list(centroids)
    
        #Computing updated centroid points
        while (count<cluster_count):
            centroids[count] = sum(clusters[count])/len(clusters[count])
            count+=1

        #Computing sum of squared error
        sse = sse_calculation(centroids,old_centroids)
        
        iteration_count +=1
        
        #To check if the algorithm reached it's convergence
        if (sse < epsilon):
            convergence_variable = 4
        
    #Question 2
    print("2) Number of iterations")
    print(iteration_count)
    
    #Question 3a
    print("3a) Final mean Values")
    print([l.tolist() for l in centroids])
    
    #Question 3b
    print("3b) Sum of Square Error")
    print(sse)
    
    #Question 4
    count  = 0
    print("4) Final Cluster Assignments")
    while count < cluster_count:
        print("Cluster",count)
        cs = [l.tolist() for l in clusters[count]]
        count+=1
        print(cs)
    print("4) Respective id points")
    print(ids)
    
    #Question 5
    print("5) Size of each clusters")
    count = 0
    while(count<cluster_count):
        print(len(clusters[count]))
        count+=1
    
    return ids,centroids

           
#Function call - kmeans algorithm    
cluster_assignment,centroid_points = kmeans()
