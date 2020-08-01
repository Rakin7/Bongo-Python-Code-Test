# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:33:06 2020

@author: Rakin
"""
def print_depth(data, depth=1):
    for i in data:
        print(i, depth)
        if isinstance(data[i], dict): #checks if dictionary or not
            print_depth(data[i], depth+1)