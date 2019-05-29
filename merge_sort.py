# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:36:24 2019

@author: Valmir
"""

import sys
import numpy as np
import random
import time

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    
    L = np.zeros(n1 + 1)
    R = np.zeros(n2 + 1)
    
    for i in range(0, n1):
        L[i] = A[p+i]
        
    for j in range(0, n2):
        R[j] = A[q+j+1]
        
    L[n1] = float('+inf')
    R[n2] = float('+inf')
    
    i = 0
    j = 0
    k = p
    
    while k < (r+1):
        if L[i] < R[j]:
            A[k] = L[i]
            k += 1
            i += 1
        else:
            A[k] = R[j]
            k += 1
            j += 1
        

def merge_sort(A, p, r):
    if p < r:
        q = (p+r)/2
        merge_sort(A, int(p), int(q))
        merge_sort(A, int(q+1), int(r))
        merge(A, int(p), int(q), int(r))
    

def executar_merge_sort(start, stop, step, n_iterations, LIMITE_ALEATORIO, name_file):
    file = open(name_file, "w+")
    
    file.write("MergeSort: start=" + str(start) + ", stop=" + str(stop) + ", step=" + str(step) + ", n_iterations=" + str(n_iterations))
    file.write("\n")
    file.write("Size= Array Size, mean= Mean Execution Time (nanoseconds), standardDeviation = Standard Deviation (nanoseconds)")
    file.write("\n")
    
#    Define problem size:
    for i in range(start, stop+1, step):
#        Repeat experiment nIteration times
        mean_execution_time = int(0)
        min_execution_time = sys.maxsize
        
        for j in range(0, n_iterations):
#            Initialize Array
            A = np.zeros(i)
            
            for k in range(0, i):
                A[k] = random.random() * LIMITE_ALEATORIO
            
            start_time = time.time_ns()
            merge_sort(A, int(0), int(len(A)-1));
            end_time = time.time_ns()
            execution_time = end_time - start_time
            
            mean_execution_time += execution_time
            
            if execution_time < min_execution_time:
                min_execution_time = execution_time
                
#       print(execution_time)
        mean_execution_time = int(mean_execution_time / n_iterations)
        standard_deviation = int(mean_execution_time - min_execution_time)
       
        file.write(str(i)+" "+str(mean_execution_time)+" "+str(standard_deviation)+"\n")
    
    file.close()
    