# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import numpy as np
import matplotlib.pyplot as plt
import math


class BTree:
    def __init__(self,data,child=[],isLeaf=True,max_data=5):  
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data
        
    def Insert(T,i):
        if not IsFull(T):
            InsertInternal(T,i)
        else:
            m, l, r = Split(T)
            T.data =[m]
            T.child = [l,r]
            T.isLeaf = False
            k = FindChild(T,i)  
            InsertInternal(T.child[k],i) 
            
    def InsertInternal(T,i):
        # T cannot be Full
        if T.isLeaf:
            InsertLeaf(T,i)
        else:
            k = FindChild(T,i)   
            if IsFull(T.child[k]):
                m, l, r = Split(T.child[k])
                T.data.insert(k,m) 
                T.child[k] = l
                T.child.insert(k+1,r) 
                k = FindChild(T,i)  
            InsertInternal(T.child[k],i) 
    def FindChild(T,k):
        # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
        for i in range(len(T.data)):
            if k < T.data[i]:
                return i
        return len(T.data)
    def Split(T):
        #print('Splitting')
        #PrintNode(T)
        mid = T.max_data//2
        if T.isLeaf:
            leftChild = BTreeClass(T.data[:mid],max_data=T.max_data) 
            rightChild = BTreeClass(T.data[mid+1:],max_data=T.max_data) 
        else:
            leftChild = BTreeClass(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
            rightChild = BTreeClass(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
        return T.data[mid], leftChild,  rightChild 
    def IsFull(T):
        return len(T.data) >= T.max_data
    
    def Height(T):
        if T.isLeaf:
            return 0
        return 1 + Height(T.child[0]) 
    
    def Search(T,k):
        # Returns node where k is, or None if k is not in the tree
        if k in T.data:
            return T
        if T.isLeaf:
            return None
        return Search(T.child[FindChild(T,k)],k)
        
    
    def NumItems(T):
        if T.isLeaf:
            return len(T.data)
        items = len(T.data)
        for i in T.child:
            items += NumItems(i)
        return items

class BTreeClass(object):
    # Constructor
    def __init__(self,data,child=[],isLeaf=True,max_data=5):  
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data
        
    

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        if k < T.data[i]:
            return i
    return len(T.data)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTreeClass(T.data[:mid],max_data=T.max_data) 
        rightChild = BTreeClass(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTreeClass(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
        rightChild = BTreeClass(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
    return T.data[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.data.append(i)  
    T.data.sort()

def IsFull(T):
    return len(T.data) >= T.max_data

def Leaves(T):
    # Returns the leaves in a b-tree
    if T.isLeaf:
        return [T.data]
    s = []
    for c in T.child:
        s = s + Leaves(c)
    return s

        
def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.data =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
     
def Height(T):
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[0])    
    
def Print(T):
    # Prints data in tree in ascending order
    if T.isLeaf:
        for t in T.data:
            print(t,end=' ')
    else:
        for i in range(len(T.data)):
            Print(T.child[i])
            print(T.data[i],end=' ')
        Print(T.child[len(T.data)])    
         
def PrintD(T,space):
    # Prints data and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i])
    else:
        PrintD(T.child[len(T.data)],space+'   ')  
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i])
            PrintD(T.child[i],space+'   ')
 
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.data:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)

def Set_x(T,Dx):
    # Finds x-coordinate to display each node in the tree
    if T.isLeaf:
        return 
    else:
        for c in T.child:
            Set_x(c,Dx)
        d = (Dx[T.child[0].data[0]] + Dx[T.child[-1].data[0]] + 10*len(T.child[-1].data))/2
        Dx[T.data[0]] = d - 10*len(T.data)/2


def DrawBtree_(T, Dx, y, y_inc, fs, ax):
    # Function to display b-tree to the screen 
    # It works fine for trees with up to about 70 data
    xs = Dx[T.data[0]]
    if T.isLeaf:
        for itm in T.data:
            ax.plot([xs,xs+10,xs+10,xs,xs],[y,y,y-10,y-10,y],linewidth=1,color='k')
            ax.text(xs+5,y-5, str(itm), ha="center", va="center",fontsize=fs)
            xs +=10
    else:
        for i in range(len(T.data)):
            xc = Dx[T.child[i].data[0]] + 5*len(T.child[i].data)
            ax.plot([xs,xs+10,xs+10,xs,xs],[y,y,y-10,y-10,y],linewidth=1,color='k')
            ax.text(xs+5,y-5, str(T.data[i]), ha="center", va="center",fontsize=fs)
            ax.plot([xs,xc],[y-10,y-y_inc],linewidth=1,color='k')
            DrawBtree_(T.child[i], Dx, y-y_inc, y_inc, fs, ax)
            xs +=10
        xc = Dx[T.child[-1].data[0]] + 5*len(T.child[-1].data)
        ax.plot([xs,xc],[y-10,y-y_inc],linewidth=1,color='k')
        DrawBtree_(T.child[-1], Dx, y-y_inc, y_inc, fs, ax)
    
def DrawBtree(T):
    #Find x-coordinates of leaves    
    LL = Leaves(T)
    Dx ={}
    d =0
    for L in LL:
        Dx[L[0]]=d 
        d += 10*(len(L)+1)  
    #Find x-coordinates of internal nodes
    Set_x(T,Dx)    
    #plt.close('all')
    fig, ax = plt.subplots()
    DrawBtree_(T, Dx, 0, 30, 10, ax)
    ax.set_aspect(1.0)
    ax.axis('off') 
    plt.show()
    
    
def Smallest(T):
    if T.isLeaf:
        return T.data[0]
    return Smallest(T.child[0])

def Largest(T):
    if T.isLeaf:
        return T.data[-1]
    return Largest(T.child[-1])

def NumItems(T):
    if T.isLeaf:
        return len(T.data)
    items = len(T.data)
    for i in T.child:
        items += NumItems(i)
    return items
    
def LargestDepth(T,d):
    if T.isLeaf:
        return T.data[-1]
    if d == 0:
        return T.data[-1]
    return LargestDepth(T.child[-1],d-1)

def PrintItemsNode(T,k):
    t = Search(T,k)
    if t != None:
        print(T.data)       
    
def Range(T):
      return Largest(T) - Smallest(T)  
  

def SumAtDepthD(T,d):
     Sum = 0
     l = 0
     if d == 0:
      for i in range(len(T.data)-1,-1,-1):
         Sum += T.data[i]
      return Sum 
     if T.isLeaf:
      return 0
     for i in range (len(T.child)):
      l += SumAtDepthD(T.child[i],d-1)
     return l
 
def IsFullNode(T,k):
    t = T.Search(T,k)
    if t == None:
        return False
    return T.IsFull(t)

if __name__ == "__main__":    
    plt.close('all')
    T = BTree([],max_data=5)  
    #T = BTree([],max_data=3)  
    #T = BTree([],max_data=7)  
    #L = np.random.permutation(42)
    L = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21]
    for i in L:
        Insert(T,i)
#        DrawBtree(T)
        
#    print('Keys in the tree: ')
#    Print(T) 
#    print()
    
    print('Tree structure')
    PrintD(T,'') 
#    DrawBtree(T)
    
#    print ('Smallest Element: ',Smallest(T))
#    
#    print ("Largest Element: ",Largest(T))
#    
#    print ("Number of items: ", NumItems(T))
#    
#    print ("Largest at Depth: ", LargestDepth(T,2))
    
    print ("Range:",Range(T))
    
   
    
   