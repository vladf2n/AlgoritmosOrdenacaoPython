# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:36:24 2019

@author: Valmir
"""

import sys
import numpy as np
import random
import time

def exchange(A, i, j):
    aux = A[i]
    A[i] = A[j]
    A[j] = aux
    

def partition(A, p, r):
    x = A[r]
    i = p-1
    
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            exchange(A, int(i), int(j))
    
    exchange(A, i+1, r)
    
    return i+1
    

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
    

def executar_quick_sort(start, stop, step, n_iterations, LIMITE_ALEATORIO, name_file):
    file = open(name_file, "w+")
    
    file.write("QuickSort: start=" + str(start) + ", stop=" + str(stop) + ", step=" + str(step) + ", n_iterations=" + str(n_iterations))
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
            quick_sort(A, int(0), int(len(A)-1));
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
    