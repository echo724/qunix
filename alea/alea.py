#!/usr/bin/env python
# coding: utf-8
import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from microqiskit import *

def q_rand_filename():
    q_num, c_num = 7, 7
    circuit = QuantumCircuit(q_num,c_num)
    for i in range(q_num):
        circuit.h(i)
        circuit.measure(i,i)
        
    result = simulate(circuit, shots = 1, get='memory')
    rand_num = int(result[0], 2) % 30 #(2**(q_num-1))
    file_name = format(rand_num, '02') + '.txt'
    
    return file_name


def comment_feeling(feeling):
    file_name = q_rand_filename()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("-"*30)
    # fortume
    with open("./fortune_box/fortune/"+file_name, "r") as file:
        print(file.read())
    
    print("-"*30)
    # emoticon
    with open("./fortune_box/emotion/"+feeling+".txt", "r", encoding='UTF8') as file:
        print(file.read())

parser = argparse.ArgumentParser(description='''\
Random Qauntum Quotes Generator using Quantum's Superposition

Usage
---------
python alea -f (emotion)
---------

- Shows the random quotes related Quantum
- Measuring quantum's superposition state gives randomness
- Can change the emoji of output by entering emotion arguments

''',formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-f', help='''\
Emotions List
---------------
angry
boring
crazy
dissastifaction
dog
embarrassed
excited
happy
joy
sad
sleepy
stupid\
'''
, default="happy", type=str)

args = parser.parse_args()

comment_feeling(args.f)




