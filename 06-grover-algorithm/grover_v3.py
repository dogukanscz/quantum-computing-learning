from math import floor, pi, sqrt

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

target = input("enter target state: ").strip()

if len(target) < 2 or any(bit not in "01" for bit in target):
    raise ValueError("please enter at least two binary digits")

# calculate the number of grover iterations
qubit_count = len(target)
state_count = 2 ** qubit_count
grover_iterations = floor((pi / 4) * sqrt(state_count))

last_qubit = qubit_count - 1
control_qubits = list(range(qubit_count - 1))

circuit = QuantumCircuit(qubit_count, qubit_count)

# equal superposition
circuit.h(range(qubit_count))

for _ in range(grover_iterations):

    # oracle
    for qubit, bit in enumerate(reversed(target)):
        if bit == "0":
            circuit.x(qubit)

    circuit.h(last_qubit)
    circuit.mcx(control_qubits, last_qubit)
    circuit.h(last_qubit)

    for qubit, bit in enumerate(reversed(target)):
        if bit == "0":
            circuit.x(qubit)

    # diffuser
    circuit.h(range(qubit_count))
    circuit.x(range(qubit_count))

    circuit.h(last_qubit)
    circuit.mcx(control_qubits, last_qubit)
    circuit.h(last_qubit)

    circuit.x(range(qubit_count))
    circuit.h(range(qubit_count))

circuit.measure(
    range(qubit_count),
    range(qubit_count)
)

# show the circuit
circuit.draw("mpl")

# run with simulator
sampler = StatevectorSampler()
job = sampler.run([circuit], shots=1024)
result = job.result()

# show results
counts = result[0].data.c.get_counts()

print("target:", target)
print("iterations:", grover_iterations)
print("result:", counts)

plot_histogram(counts)
plt.show()