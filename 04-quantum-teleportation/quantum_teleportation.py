from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

circuit = QuantumCircuit(3, 1)

# create a bell pair between q1 and q2
circuit.h(1)
circuit.cx(1, 2)

circuit.x(0) # prepare q0 as |1>

# connect q0 to the bell pair
circuit.cx(0,1)
circuit.h(0)

# apply the corrections to q2
circuit.cx(1,2)
circuit.cz(0,2)

circuit.measure(2,0) # measure only q2

# show the circuit
print(circuit.draw("text"))

#shot 1024 times with quantum simulator
sampler = StatevectorSampler()
job = sampler.run([circuit], shots=1024)
result = job.result()

#measurement results
counts = result[0].data.c.get_counts()
print("q2 measurement after teleporting |1> ",counts)

plot_histogram(counts)
plt.show()