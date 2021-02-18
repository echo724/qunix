import argparse

def argparsing():
    parser = argparse.ArgumentParser(description='''Build Quantum Circuit usign MicroQiskit
    It will read arguments, build quantum circuit based on them, and show the result of simulation(Default Result: Counts)\
    ''',formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-q', type=int, nargs=1,
                        help='An integer for adding quantum bits',required=True)
    parser.add_argument('-c', type=int, nargs=1,
                        help='An integer for adding classical bits',required=True)
    parser.add_argument('--prob', help='Return probabilities as the result',action="store_true")
    parser.add_argument('--state', help='Return statevector as the result',action="store_true")
    parser.add_argument(nargs="+",metavar="gates",dest="gates",help='''\
    String for applying gate and its position
    Input Type
    --------------------
    h a: Hadamard gate at qubit a
    x a: X gate at qubit a
    y a: Y gate at qubit a
    z a: Z gate at qubit a
    rx a b: RX gate at qubit b by rotating a
    rz a b: RZ gate at qubit b by rotating a
    ry a b: RY gate at qubit b by rotating a
    cx a b: CNOT gate at control a, target b
    crx a b o: CRX gate at control b, target o by rotating a
    m a b: Measure at qubit a to clbit b
    m 'all': Measure all qubits
    --------------------\
    ''')
    args = parser.parse_args()

    assert args.q[0] > 0, "Qbit number must be bigger than 0"
    assert args.c[0] > 0, "Clbit number must be bigger than 0"
    assert not((args.state) and (args.prob)), "Reesult type must be one type"

    instruct = args.gates[0].split(" ")

    assert len(instruct) > 0, "Gate arguments is not entered"

    return args.q[0], args.c[0], args.prob,args.state, instruct