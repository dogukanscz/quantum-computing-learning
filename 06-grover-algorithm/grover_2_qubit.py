from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

circuit = QuantumCircuit(2,2)

#equal superposition
circuit.h(0)
circuit.h(1)

#oracle marks |11>
circuit.cz(0,1)

# ORACLE: |00>
# circuit.x(0)
# circuit.x(1)
# circuit.cz(0, 1)
# circuit.x(0)
# circuit.x(1)

# ORACLE: |01>
# circuit.x(0)
# circuit.cz(0, 1)
# circuit.x(0)

# ORACLE: |10>
# circuit.x(1)
# circuit.cz(0, 1)
# circuit.x(1)

#grover diffuser HH->XX->CZ->XX->HH
circuit.h(0)
circuit.h(1)

circuit.x(0)
circuit.x(1)

circuit.cz(0,1)

circuit.x(0)
circuit.x(1)

circuit.h(0)
circuit.h(1)

circuit.measure([0,1],[0,1])

# show the circuit
print(circuit.draw("text"))

#shot 1024 times with quantum simulator
sampler = StatevectorSampler()
job = sampler.run([circuit], shots=1024)
result = job.result()

#get measurement results
counts = result[0].data.c.get_counts()
print(counts)

plot_histogram(counts)
plt.show()