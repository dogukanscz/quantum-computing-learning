from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

circuit = QuantumCircuit(2,1)
circuit.h(0)

#phase kickback
circuit.x(1)
circuit.h(1)

# balanced oracle f(x) = x
circuit.cx(0,1)

circuit.h(0)
circuit.measure(0,0)


# show the circuit
circuit.draw("mpl")

#shot 1024 times with quantum simulator
sampler = StatevectorSampler()
job = sampler.run([circuit], shots=1024)
result = job.result()

#get measurement results
counts = result[0].data.c.get_counts()
print(counts)

plot_histogram(counts)
plt.show()
