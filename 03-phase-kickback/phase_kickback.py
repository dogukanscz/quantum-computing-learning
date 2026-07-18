from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

circuit = QuantumCircuit(2, 1) # 2 qubits and 1 classical bits
circuit.h(0) # put q0 into superposition |+>
circuit.x(1) # X|0> = |1>
circuit.h(1) # H|1> = |->
circuit.cx(0, 1) # x on |-> adds a negative phase to the q0 = 1 branch
circuit.h(0) # changes q0 from |-> to |1>
circuit.measure(0, 0) # measure q0

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