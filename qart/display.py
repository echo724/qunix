import sys
import os
from contextlib import contextmanager
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout
with suppress_stdout():
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    from qcb.parse import argparsing
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import microqiskit as mq

def backend():
    try:
        qn,cn,_,_,instruct = argparsing()
    except SystemExit:
        qc = 5
        cn = 5
        instruct = ['h','0','h','1','h','2','h','3','h','4','m','.']

    qc = mq.QuantumCircuit(qn,cn)

    try:
        for i in range(len(instruct)):
            if instruct[i].isalpha():
                if instruct[i] == "h":
                    qc.h(int(instruct[i+1]))
                if instruct[i] == "x":
                    qc.x(int(instruct[i+1]))
                if instruct[i] == "y":
                    qc.y(int(instruct[i+1]))
                if instruct[i] == "z":
                    qc.z(int(instruct[i+1]))
                if instruct[i] == "cx":
                    qc.cx(int(instruct[i+1]),int(instruct[i+2]))
                if instruct[i] == "rx":
                    qc.rx(float(instruct[i+1]),int(instruct[i+2]),int(instruct[i+3]))
                if instruct[i] == "rz":
                    qc.rz(float(instruct[i+1]),int(instruct[i+2]),int(instruct[i+3]))
                if instruct[i] == "ry":
                    qc.ry(float(instruct[i+1]),int(instruct[i+2]),int(instruct[i+3]))
                if instruct[i] == "crx":
                    qc.crx(float(instruct[i+1]),int(instruct[i+2]),int(instruct[i+3]))
                if instruct[i] == "m":
                    try:
                        if instruct[i+1] == ".":
                            for j in range(qn):
                                qc.measure(j,j)
                        else:
                            qc.measure(int(instruct[i+1]),int(instruct[i+1]))
                    except Exception as e:
                        print("Instruction of measurement is Invalid. Please check the measurement:", e)
            else:
                continue
    except:
        print("Invalid instruction arguments. Please Check the arguments")

    return qc

def get_output_source(qc,w,h):
    return mq.simulate(qc,shots=((60//qc.num_qubits)*20),get="memory")

def output(n=300,w=60,h=20):
    
    qc = backend()

    for i in range(n):
        output_source = get_output_source(qc,w,h)
        
        line = ""
        packed = []
        for i in range(len(output_source)):
            line += output_source[i]
            if len(line) > w:
                packed.append(line)
                line = ""
            else:
                continue
        for i in packed:
            for j in i:
                if j == "1":
                    print("◼",end="")
                else:
                    print("◻︎",end="")
            print("")
        sleep(0.1)
        clear()

n = int(input("Seconds: "))
output(n*10)