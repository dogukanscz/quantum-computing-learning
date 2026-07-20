from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

#secretNumber = '1000101'
circuit = QuantumCircuit(8,7)

circuit.h([0,1,2,3,4,5,6])

#phase kickback
circuit.x(7)
circuit.h(7)

circuit.barrier()

#Positions with a value of 1
circuit.cx(6,7)
circuit.cx(2,7)
circuit.cx(0,7)

circuit.barrier()
circuit.h([0,1,2,3,4,5,6])

circuit.measure([0,1,2,3,4,5,6],[0,1,2,3,4,5,6])


# show the circuit
circuit.draw("mpl")

# run the circuit one time
sampler = StatevectorSampler()
job = sampler.run([circuit], shots=1)
result = job.result()

#get measurement results
counts = result[0].data.c.get_counts()
print(counts)

plot_histogram(counts)
plt.show()
