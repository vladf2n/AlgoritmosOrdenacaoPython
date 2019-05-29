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

        
def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A, i, heap_size):
    l = left(int(i))
    r = right(int(i))
    
    if l < heap_size and A[l] > A[i]:
        lagest = l
    else:
        lagest = i
        
    if r < heap_size and A[r] > A[lagest]:
        lagest = r
    
    if lagest != i:
        exchange(A, int(i), int(lagest))
        max_heapify(A, int(lagest), int(heap_size))
    

def build_max_heap(A):
    for i in range(int(((len(A)/2) - 1)), -1, -1):
        max_heapify(A, int(i), int(len(A)))
    

def heap_sort(A):
    heap_size = len(A)
    build_max_heap(A)
    
    for i in range(len(A)-1, 0, -1):
        exchange(A, int(0), int(i))
        heap_size -= 1
        max_heapify(A, int(0), int(heap_size))
    

def executar_heap_sort(start, stop, step, n_iterations, LIMITE_ALEATORIO, name_file):
    file = open(name_file, "w+")
    
    file.write("HeapSort: start=" + str(start) + ", stop=" + str(stop) + ", step=" + str(step) + ", n_iterations=" + str(n_iterations))
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
            heap_sort(A);
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
    