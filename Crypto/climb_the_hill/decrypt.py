#!/usr/bin/env python3
import numpy as np
from sympy import *
import itertools

def encrypt(ciphertext, key, char_set):
    key = Matrix(key)
    # Calculate inverse of the Key matrix(mod N) where N = no. of chars in alphabet
    inv_key = key.inv_mod(39)       

    pt = ''
    # Loop through n chars at a time when Key matrix is n x n
    for i in range(0, len(ciphertext), 3):
        chars = ciphertext[i : i+3]     
        chars_index = [char_set.index(ch) for ch in chars] 
        res = np.dot(inv_key, chars_index) % 39         # matrix mult and (mod N)
        pt += ''.join(char_set[int(i)] for i in res)
    return pt

key = [ [6, 24, 11],         # key matrix
        [12, 13, 10], 
        [20, 17, 15]
    ]       

char_set = "abcdefghijklmnopqrstuvwxyz0123456789{}_"
cipherText = "z3{ryu0kdhhxwuph__oin4}{h5cn78y6a{obebxbh932j"


print(f"Decrypted Text: " + encrypt(cipherText,key,char_set))    