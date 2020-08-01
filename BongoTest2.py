# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:40:02 2020

@author: Rakin
"""
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

        
def print_depth(data, depth=1):
    if isinstance(data, Person):
        print("first_name:", depth)
        print("last_name:", depth)
        print("father:", depth)
        if isinstance(data.father, Person):
            print_depth(data.father, depth+1)

    elif isinstance(data, dict):
        for i in data:
            print(i, depth)
            if isinstance(data[i], object):
                print_depth(data[i], depth+1)

