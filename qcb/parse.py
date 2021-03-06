#!/usr/bin/env python

import argparse

def argparsing():
    parser = argparse.ArgumentParser(description='''\
    QCB
    ===

    Build Quantum Circuit using MicroQiskit

    - By entering one line arguemnts, it will build Quantum Circuit and get the result of its simulation
    - The default result type is counts, but `--prob` and `--state` will change the result type
    - For the syntax of gate instruction, see the Gate Type below

    Simple Usage
    ------------------------------------------------------------
    qcb -q 2 -c 2 (--prob)(--state) "h 0 cx 0 1 m ."
    ------------------------------------------------------------
    \
    ''',formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-q', type=int, nargs=1,default=2,
                        help='An integer for adding quantum bits')
    parser.add_argument('-c', type=int, nargs=1,default=2,
                        help='An integer for adding classical bits')
    parser.add_argument('--prob', help='Return probabilities as the result',action="store_true")
    parser.add_argument('--state', help='Return statevector as the result',action="store_true")
    parser.add_argument(nargs="+",metavar="gates",default="h 0 h 1 m .",dest="gates",help='''\
    String for applying gate and its position
    Gate Type
    --------------------
    h a: Hadamard gate at qubit a
    x a: X gate at qubit a
    y a: Y gate at qubit a
    z a: Z gate at qubit a
    rx a b: RX gate at qubit b by rotating a
    rz a b: RZ gate at qubit b by rotating a
    ry a b: RY gate at qubit b by rotating a
    cx a b: CNOT gate at control a, target b
    crx a b c: CRX gate at control b, target c by rotating a
    m a b: Measure at qubit a to clbit b
    m .: Measure all qubits
    --------------------\
    ''')

    args = parser.parse_args()

    assert args.q[0] > 0, "Qbit number must be bigger than 0"
    assert args.c[0] > 0, "Clbit number must be bigger than 0"
    assert not((args.state) and (args.prob)), "Reesult type must be one type"

    instruct = args.gates[0].split(" ")

    assert len(instruct) > 0, "Gate arguments is not entered"

    return args.q[0], args.c[0], args.prob,args.state, instruct
