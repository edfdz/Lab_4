#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:23:58 2019

@author: eduardofernandez
"""
import numpy as np

class WordEmbedding(object):
    def __init__(self,word,embedding):
        # word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)
        
    def __gt__(self,other):
        if isinstance(other, WordEmbedding): return self.word > other.word
        return self.word > other
    
    def __lt__(self,other):
        if isinstance(other, WordEmbedding): return self.word < other.word
        return self.word < other
    
    def __eq__(self,other):
        if isinstance(other, WordEmbedding): return self.word == other.word
        return self.word == other
    
    def __repr__(self):
        return self.word