from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# create the circuit
circuit = QuantumCircuit(2, 2)

# put q0 into superposition
circuit.h(0)

# connect q0 and q1
circuit.cx(0, 1)

# measure both qubits
circuit.measure([0, 1], [0, 1])

# show the circuit
print(circuit.draw("text"))

# run the circuit 1024 times
sampler = StatevectorSampler()
job = sampler.run([circuit], shots=1024)
result = job.result()

# get the measurement results
counts = result[0].data.c.get_counts()
print(counts)

# show the results
plot_histogram(counts)
plt.show()