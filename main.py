# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:42:59 2019

@author: Valmir
"""

import sys
from insertion_sort import executar_insertion_sort
from heap_sort import executar_heap_sort
from merge_sort import executar_merge_sort
from merge_sort_hibrid import executar_merge_sort_hibrid
from quick_sort import executar_quick_sort
from quick_sort_hibrid import executar_quick_sort_hibrid

def main(start, stop, step, n_iterations, LIMITE_ALEATORIO, LIMITE):
    
    name_file = "_I"+str(start)+"_F"+str(stop)+"_P"+str(step)+"_N"+str(n_iterations)+"_A"+str(LIMITE_ALEATORIO)+".txt"
    
    executar_insertion_sort(start, stop, step, n_iterations, LIMITE_ALEATORIO, "insertionSort"+name_file)
    executar_heap_sort(start, stop, step, n_iterations, LIMITE_ALEATORIO, "heapSort"+name_file)
    executar_merge_sort(start, stop, step, n_iterations, LIMITE_ALEATORIO, "mergeSort"+name_file)
    executar_merge_sort_hibrid(start, stop, step, n_iterations, LIMITE_ALEATORIO, LIMITE, "mergeSortHibrid"+name_file)
    executar_quick_sort(start, stop, step, n_iterations, LIMITE_ALEATORIO, "quickSort"+name_file)
    executar_quick_sort_hibrid(start, stop, step, n_iterations, LIMITE_ALEATORIO, LIMITE, "quickSortHibrid"+name_file)
    
if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))