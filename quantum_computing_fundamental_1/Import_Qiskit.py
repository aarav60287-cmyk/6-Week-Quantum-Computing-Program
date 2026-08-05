from qiskit import QuantumCircuit
import qiskit

qc=qiskit.QuantumCircuit(1)
qc.h(0)
qc.measure_all()
print(qc)