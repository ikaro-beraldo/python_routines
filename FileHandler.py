#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:53:34 2020

@author: Ikaro Beraldo
"""
#Graphical interfaces functions to handle MatLab files
class MatFileHandler:
    
        
    #Method to extract variables from .mat files
    def open_mat_file():    
        #Import tkinter (module for graphical interfaces)
        import tkinter as tk
        from tkinter import filedialog
            
        #Class for the main window of the application (tk.Tk())
        root = tk.Tk()
        #Withdram a widget from the screen (avoid the maintenance of a little
        #window)
        root.withdraw()
        
        #Execute the method (opens the dialog box and select the file path; returns
        # the file path as the var 'file_path')
        file_path = filedialog.askopenfilename()
        
        #Print the selected file path
        print('Selected File:',file_path)
        
        #return the selected file path
        return file_path
    
    
    #Convert the MatLab file into Python HDF5 file system
    def mat_to_py(mat_file_path):
        #mat_file_path = path to .mat file that is going to be converted
        #Import the loadmat function from the scipy.io module (it loads the .mat file)
        from scipy.io import loadmat
        #Loads the MatLab file
        imported_data = loadmat(mat_file_path,mat_dtype='False')
        
        #Returns the imported_data, now as a python dict
        return imported_data
    
    #Method to load the selected file
    def save_mat_file(self):
        #Import tkinter (module for graphical interfaces)
        import tkinter as tk
        #Import the file dialog module (creates the file dialog to choose the file path)
        from tkinter import filedialog
        
        import h5py
        
        #Import module to load matlab files
        from scipy.io import loadmat
    
        
        #Class for the main window of the application (tk.Tk())
        root = tk.Tk()
        #Withdram a widget from the screen (avoid the maintenance of a little
        #window)
        root.withdraw()
        
        #Execute the method (opens the dialog box and select the file path; returns
        # the file path as the var 'file_path')
        file_path = filedialog.asksaveasfile()
        
                
        #Print the selected file path
        print('Selected File: ',file_path)
        