# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:12:48 2020

@author: Rakin
"""
import copy
def lca(node1, node2):
    a = copy.deepcopy(node1)
    depth1=0
    while a.parent:
        a = a.parent
        depth1 += 1        
    b = copy.deepcopy(node2)
    depth2=0
    while b.parent:
        b = b.parent
        depth2 += 1
    x = copy.deepcopy(node1)
    y = copy.deepcopy(node2)
    while depth1 != depth1:
        if depth1 > depth2:
            x = node1.parent
            depth1 -= 1
        else:
            y = node2.parent
            depth2 -= 1
    while x.value != y.value:
        x = x.parent
        y = y.parent
    return x

