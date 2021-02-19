#!/usr/bin/env python
# coding: utf-8
import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
    # fortume
    with open("./fortune_box/fortune/"+file_name, "r") as file:
        longest = 0
        quote = file.read()
        splitted = quote.split("\n")
        nextline = ""
        for line in splitted:
            line += nextline
            if len(line) > longest and len(line) < 75:
                longest = len(line)
            if len(line) > 74:
                longest = 75
                nextline = line[75:]
        longest += 1
        print("","-"*longest," ")
        for i,line in enumerate(splitted):
            line += nextline
            nextline = ""
            if len(line) > 74:
                nextline = line[75:]
                line = line[:74]
            print("|","",end="")
            print(line,end="")
            print(" "*(longest - len(line) - 1),"|")
        while len(nextline) > 0:
            print("|","",end="")
            remain=len(nextline)
            if remain > 75:
                print(nextline[:75],end="")
                print("","|")
                nextline = nextline[75:]
            else:
                print(nextline,end="")
                print(" "*(longest - len(nextline) - 1),"|")
                break

        print("","-"*longest," ")
    print("")
    # emoticon
    with open("./fortune_box/emotion/"+feeling+".txt", "r", encoding='UTF8') as file:
        print(file.read())
        print("")

parser = argparse.ArgumentParser(description='''\
Alea
====

Random Quantum Quotes Generator from measuring qubit's superposition state

- Measuring qubit's superposition state give random classical bit
- It picks the Quotes randomly by using this
- Can change the Ascii Emoji by using -f flag (available emotions are in Emotions List below)

Usage
---------------------------------------------
alea -f (emotion)
---------------------------------------------
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




