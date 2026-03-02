from app.problem_mapper import map_to_quantum
from app.optimizer import optimize_for_hardware
from app.quantum_solver import execute_quantum
from app.postprocess import process_result
from qiskit_aer import AerSimulator

def run_pipeline():
    edges = [(0, 1), (1, 2), (2, 0)]
    operator, offset = map_to_quantum(edges)
    backend = AerSimulator()
    circuit = optimize_for_hardware(operator, backend)
    result = execute_quantum(circuit)
    solution = process_result(result)
    return solution

if __name__ == "__main__":
    print("Best cut:", run_pipeline())
