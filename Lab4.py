#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:02:48 2019

@author: eduardofernandez
"""


from timeit import time as time
import codecs
import numpy as np

from BTrees import BTree

from BST import BSTLab

from WordEmbedding import WordEmbedding

def readData(filename):
    data = []
    with codecs.open(filename,"r","utf_8_sig") as f:
        for line in f:
            chunks = line.split()
            word, embedding = chunks[0], np.array([float(value) for value in chunks[1:]])
            data.append(WordEmbedding(word, embedding))
    return data

def ReadPairs(filename):
    data = []
    with codecs.open(filename,"r","utf_8_sig") as f:
        for line in f:
            data.append(tuple(map(lambda x: x.strip(), line.split(","))))
    return data

def CalSimilarity(e1,e2):
    return np.dot(e1,e2) / ((np.linalg.norm(e1) * np.linalg.norm(e2)))

if __name__ == "__main__":  
    
    TxtFilename = "glove.6B.50d.txt"
    pairFilename = "pair.txt"
    
    
    print ('Choose table implementation.')
    print ('Type 1 for binary search tree or 2 for B-Tree')
    word = int(input('Choice: '))
    
    if (word == 1):
        T = BSTLab()
        print ("Building BST: ")
        tempFile = readData(TxtFilename)
        start = time.time()
        for x in tempFile: T.Insert(x)
        end = time.time()
        total = (end - start)
        print("stats: ")
        print("stats: ")
        print("Number of nodes: ", T.NumItems())
        print("Height: ", T.Height())
        print("Running Time for construction: ", total)
    elif (word == 2):
        n = int(input("Maximum number of nodes: "))
        T = BTree([],n)
        print ("Building BTree: ")
        tempFile = readData(TxtFilename)
        start = time.time()
        for x in tempFile: T.Insert(x)
        end = time.time()
        total = (end - start)
        print("stats: ")
        print("Number of nodes: ", T.NumItems())
        print("Height: ", T.Height())
        print("Running Time for construction: ", total)
    else:
        print ('Incorrect input')
        
    pair = ReadPairs(pairFilename)
    print ("Word similarities found: ")
    total = 0
    for (x0,x1) in pair:
        start = time.time()
        e1 = T.Search(x0)
        e2 = T.Search(x1)
        end = time.time()
        total += (end - start)
        if e1 == None or e2 == None: continue
        print ("Similarity [{0},{1}] = {2:.4f}", CalSimilarity(e1,e2))
        