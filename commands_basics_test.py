#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:37:03 2020

@author: ikaro
"""

from matplotlib import pyplot as plt
from scipy.io import loadmat

#
from FileHandler import MatFileHandler
mfh = MatFileHandler()
file_path = mfh.open_mat_file()
imported_file = mfh.mat_to_py(file_path)

runfile('/mnt/f7990c0c-87ac-430f-bacf-b4bd5606a0ad/Análises/Python Routines/Basic_functions.py')

#Loads the MatLab file
annots = loadmat('/mnt/f7990c0c-87ac-430f-bacf-b4bd5606a0ad/Análises/Ikaro/Dados_Alan/R16_processed.mat',mat_dtype='False')

blocked_CH1 = np.float64(break_in_blocks(annots['C1B1'],1000,10))
blocked_CH1 = blocked_CH1[0:100,:]
#Calculate RMS
CH1_rms = root_mean_square(blocked_CH1, 2)

f, Pxx = welch_multiple_vectors(blocked_CH1,1000,1024)

srate = 1000
h_freq = 250
l_freq = 5;
filtered_data = filter.filter_data(blocked_CH1,srate,l_freq,h_freq,method='iir')
f2, Pxx2 = welch_multiple_vectors(filtered_data,1000,1024)


plt.plot(blocked_CH1[0,:])
plt.plot(filtered_data[0,:])
plt.show()

plt.plot(f,Pxx[0,:])
plt.plot(f2,Pxx2[0,:])
plt.show()