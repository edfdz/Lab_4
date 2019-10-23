#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:05:18 2019

@author: eduardofernandez
"""


import matplotlib.pyplot as plt
import numpy as np


class BSTLab(object):
    def __init__(self, data, left=None, right=None):  
        self.data = data
        self.left = left 
        self.right = right
    def Insert(T,newItem):
        if T == None:
            T =  BST(newItem)
        elif T.data > newItem:
            T.left = Insert(T.left,newItem)
        else:
            T.right = Insert(T.right,newItem)
        return T
    def search(node,k):
        if node == None:
            return
        elif node.data == k:
            return node
        elif k > node.data:
            return search(node.right,k)
        elif k < node.data:
            return search(node.left,k)
        
    def Height(T):
        if T == None:
            return 0
        lh = Height(T.left)
        rh= Height(T.right)
        return max([lh,rh])+1
    
    def NumItems(T):
        count = 1
        if T.left != None:
            count += NumItems(T.left)
        if T.right != None:
            count += NumItems(T.right)
        return count
    
        

class BST(object):
    def __init__(self, data, left=None, right=None):  
        self.data = data
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.data > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def DrawBST_(T, x0, x1, y, y_inc,ax):
    if T is not None:
        xm = (x0+x1)/2
        yn = y-y_inc
        if T.left is not None:
            p=np.array([[xm,y], [(x0+xm)/2,yn]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            DrawBST_(T.left,x0,xm,yn, y_inc,ax)
        if T.right is not None:
            p=np.array([[xm,y], [(x1+xm)/2,yn]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            DrawBST_(T.right,xm,x1,yn, y_inc,ax)
        ax.text(xm,y, str(T.data), size=10,ha="center", va="center",
            bbox=dict(facecolor='w',boxstyle="circle"))

def DrawBST(T): 
    fig, ax = plt.subplots()
    DrawBST_(T, 0, 200, 400, 20, ax)
    ax.set_aspect(1.0)
    ax.axis('off') 
    plt.show() 
    
def Inorder(node): 
  if (node is None):
      return                     
  Inorder(node.left)   
  print (node.data)                     
  Inorder(node.right) 
  
def SmallestElement(node):
    if (node.left is None):
        return node
    return SmallestElement(node.left)

def LargestElement(node):
    if (node.right is None):
        return node
    return LargestElement(node.right)

def search(node,k):
    if node == None:
        return
    elif node.data == k:
        return node
    elif k > node.data:
        return search(node.right,k)
    elif k < node.data:
        return search(node.left,k)
    
def DepthofK(T,k):
    if T== None:
        return -1
    if T.data == k:
        return 0
    if k < T.data:
        d = DepthofK(T.left,k) 
    else:
        d = DepthofK(T.right,k)
    if d == 1:
        return -1
    return d + 1
        
    
def Height(T):
    if T == None:
        return 0
    lh = Height(T.left)
    rh= Height(T.right)
    return max([lh,rh])+1
    

def PrintByDepth(T,k):
    Q=[T]
    while len(Q)>0:
        front = Q.pop(0)
        if front != None:
            print (front.data)
            Q.append(front.left)
            Q.append(front.right)
  
def ListToTree(L):
    if len(L) == 0:
        return None
    mid = len(L)/2
    return BST(L[mid],ListToTree(L[:mid]),ListToTree(L[mid:]))

def TreeToList(T):
    if T == None:
        return []
    return TreeToList(T.left)+[T.data]+ TreeToList(T.right)



if __name__ == "__main__":  
    plt.close('all')
    T = None
    A = [5,2,9,8,1,3,7]
    for a in A:
        T = Insert(T,a)
    DrawBST(T)
#    Inorder(T)
#    print (SmallestElement(T).data)
#    print (LargestElement(T).data)
#    print (search(T,10).data)
   
    