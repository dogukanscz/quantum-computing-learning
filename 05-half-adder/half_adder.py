#HALF ADDER 1+1 EXAMPLE

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

circuit = QuantumCircuit(4, 2) #q0 and q1 inputs, q2 is sum q3 is carry
circuit.x(0) # set input 1
circuit.x(1) # set input 1

# calculate sum with xor
circuit.cx(0,2)
circuit.cx(1,2)

#calculate carry with toffoli
circuit.ccx(0,1,3)

# measure sum and carry
circuit.measure(2,0)
circuit.measure(3,1)

# show the circuit
print(circuit.draw("text"))

#shot 1024 times with quantum simulator
sampler = StatevectorSampler()
job = sampler.run([circuit], shots=1024)
result = job.result()

#measurement results
counts = result[0].data.c.get_counts()
print("1+1 =",counts)

plot_histogram(counts)
plt.show()