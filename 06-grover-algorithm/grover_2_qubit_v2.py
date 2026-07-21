from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

target = input("enter target state (00, 01, 10 or 11): ").strip()

if len(target) != 2 or any(bit not in "01" for bit in target):
    raise ValueError("please enter a two bit binary number")

circuit = QuantumCircuit(2,2)

#equal superposition
circuit.h(range(2))

# mark the target state
for qubit, bit in enumerate(reversed(target)):
    if bit == "0":
        circuit.x(qubit)
circuit.cz(0, 1)

for qubit, bit in enumerate(reversed(target)):
    if bit == "0":
        circuit.x(qubit)

#grover diffuser HH->XX->CZ->XX->HH
circuit.h(range(2))

circuit.x(range(2))

circuit.cz(0,1)

circuit.x(range(2))

circuit.h(range(2))

circuit.measure(range(2),range(2))

# show the circuit
circuit.draw("mpl")

#shot 1024 times with quantum simulator
sampler = StatevectorSampler()
job = sampler.run([circuit], shots=1024)
result = job.result()

#show results
counts = result[0].data.c.get_counts()

print("target:", target)
print("result:", counts)

plot_histogram(counts)
plt.show()