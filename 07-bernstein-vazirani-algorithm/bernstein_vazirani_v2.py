from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

secretNumber = input("Please enter a binary number: ")

circuit = QuantumCircuit(len(secretNumber)+1,len(secretNumber))

circuit.h(range(len(secretNumber)))

# prepare helper qubit as |-> for phase kickback
circuit.x(len(secretNumber))
circuit.h(len(secretNumber))

circuit.barrier()

#positions with a value of 1
#oracle
for qubit, bit in enumerate(reversed(secretNumber)):
    if bit == "1":
        circuit.cx(qubit, len(secretNumber))

circuit.barrier()
circuit.h(range(len(secretNumber)))

circuit.measure(range(len(secretNumber)),range(len(secretNumber)))


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
