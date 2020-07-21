#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 02:25:07 2020

@author: ikaro_beraldo
"""

import math as ma
import numpy as np
import sys
from scipy import signal
from scipy.io import loadmat
from mne import filter

#Breaks the vetor into a multiarray data of n blocks with n samples each
def break_in_blocks(lfp_data,fs, block_length):
    #Check if the LFP data is a single dimension array
    if lfp_data.ndim == 1:
        sys.exit("Error: the LFP data must be a single dimension array")
   
    #Number of blocks
    n_block = ma.floor(lfp_data.size / (fs*block_length))
    #NUmber of samples of each block
    n_samples = fs*block_length
    
    #Excluded the remaining samples
    lfp_data = np.delete(lfp_data,np.arange(block_length*n_block*fs,len(lfp_data)))
    
    #Operation to break the blocks
    blocked_array = lfp_data.reshape((n_block,n_samples))
    
    #Return the blocked_array
    return blocked_array

#Calculate the root mean square of a vector or matrix
def root_mean_square(data,dimension):
    #If dimension = 1, the RMS will be calculate along the columns; If 2, the
    #RMS will be calculated along the rows
    if (dimension == 1): #If along columns, get the number of columns
        iterations = np.array(data.shape)[1] #number of iterations
        output_rms = np.zeros((1,iterations)) #pre-alocate the output 
        #Loop through every vector (row or column)
        for ite in np.arange(iterations):
            output_rms[ite] = np.sqrt(np.mean(np.square(data[:,ite]))) #calculate RMS

    if (dimension == 2): #If along rows, get the number of rows
        iterations = np.array(data.shape)[0] #number of iterations
        output_rms = np.zeros((iterations,1)) #pre-alocate the output 
        #Loop through every vector (row or column)
        for ite in np.arange(iterations):    
            output_rms[ite] = np.sqrt(np.mean(np.square(data[ite,:]))) #calculate RMS
    
    return output_rms

#Welch for multiple segments
def welch_multiple_vectors(data,fs,fft_number):
    #fft_number = nfft of welch calculation (Length of the FFT used)
    #fs = sampling frequency of data
    #data = multiple segments data (the calculation will be performed on each row)

    #Pre-alocate the PSD matrix
    columns = int(fft_number/2 + 1) #number of frequency components based on nfft
    rows = data.shape[0] #number of data segments
    Pxx = np.zeros((rows,columns))  #Create the pxx matrix for PSD data
    
    #iteration for each segment (row)
    for seg in np.arange(rows):
        #calculation of PSD for each segment
        f, Pxx[seg,:] = signal.welch(data[seg,:],fs,nfft = fft_number)
    
    return f, Pxx
    
        
    



