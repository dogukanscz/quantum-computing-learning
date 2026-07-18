from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

#alice wants to send "10" to bob
circuit = QuantumCircuit(2, 2) # 2 qubits and 2 classical bits
circuit.h(0) # put q0 into superposition
circuit.cx(0, 1) #cnot, end of the bell state
circuit.z(0) # use z gate for message "10"

#alice sends q0 to bob
#bob decodes the message
circuit.cx(0, 1)
circuit.h(0)
circuit.measure([0, 1], [0, 1])

# show the circuit
print(circuit.draw("text"))

#shot 1024 times with quantum simulator
sampler = StatevectorSampler()
job = sampler.run([circuit], shots=1024)
result = job.result()

#measurement results
counts = result[0].data.c.get_counts()
print(counts)

plot_histogram(counts)
plt.show()