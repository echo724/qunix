# QuNix
QuNix is a project of Unix like python programs by using Qiskit and Quantum Circuit with following Unix Philosophy

# Program lists

- Both programs use **MicroQiskit** [https://github.com/qiskit-community/MicroQiskit](https://github.com/qiskit-community/MicroQiskit)

## Quantum Circuuit Builder(QCB)
    
    - By using simple one line arguments, it will give the result of Quantum Circuit Simulation
    - It builds Quantum Circuit and get the simulation result from the circuit

### Usage

1. Clone this github repo to your machine

```Bash
$git clone https://github.com/echo724/qunix
```

2. Move to the directory of the project, and run the program
```Python
python qcb -h 2 -q 2 "h 0 cx 0 1 m all"
```

### Arguments

- **List of Arguments**

Flags|Arguments|Detail
---|---|---
-q|N|Number of Quantum Qubits
-c|N|Number of Classical Qubits
--prob|None|Show the simulation result in probabilities
--state|None|Show the simulation result in statevector
None|String|The string of **Gate instruction**

- **List of Gate Instruction** (`a,b,c is integer here`)

Gates|Syntax|Detail
---|---|---
Hadamard|h a| Hadamard gate at qubit a
X|x a| X gate at qubit a
Y|y a| Y gate at qubit a
Z|z a| Z gate at qubit a
RX|rx a b| RX gate at qubit b by rotating a
RZ|rz a b| RZ gate at qubit b by rotating a
RY|ry a b| RY gate at qubit b by rotating a
CX|cx a b| CNOT gate at control a, target b
CRX|crx a b c| CRX gate at control b, target c by rotating a
Measure|m a b| Measure at qubit a to clbit b
Measure|m 'all'| Measure all qubits

## QFortune

- It shows the random quotes related Quantum
- This randomness comes from the simulation result of measuring quantum's superposition state
- Can change the emoji of output by entering emotion arguments

### Usage

1. Clone this github repo to your machine

```Bash
$git clone https://github.com/echo724/qunix
```

2. Move to the directory of the project, and run the program


```Python
python qfortune -f joy
```

### Available Emotions

Emotion|
---|
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
stupid


# Slack Connection


# License

MicroQiskit(https://github.com/qiskit-community/MicroQiskit)
