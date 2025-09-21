import numpy as np
import time
import psutil

def simulate_random_circuit(num_qubits, depth):
    dim = 2**num_qubits
    required_memory_gb = (dim*16) / (1024**3)
    available_memory_gb = psutil.virtual_memory().available/(1024**3)

    if (required_memory_gb) > available_memory_gb:
        print("Required memory exceeds available memory")
        print("Can't scale anymore!")
        return
    
    print(f"Starting simulation now...{num_qubits} qubits...")
    # print(f"")

    state_vector = np.zeros(dim, dtype=np.complex128)
    state_vector[0] = 1.0

    for i in range(depth * num_qubits):
        pass

    probabilities = np.abs(state_vector)**2

    result_decimal = np.random.choice(range(dim), p = probabilities)
    result_bitstring = format(result_decimal, f'0{num_qubits}b')

    print(f"Classical simulation finished! Sample bitstring: {result_bitstring}")


num_qubits_small = 5
print(f" Running for SMALL problem ({num_qubits_small} qubits) ")
start_time = time.time()
simulate_random_circuit(num_qubits_small, depth = 10)
print(f"Time taken: {time.time() - start_time: .4f} seconds")

num_qubits_supremacy = 10
print(f"Attempting for 53 qubits (num_qubits_supremacy) qubits")

simulate_random_circuit(num_qubits_supremacy, depth = 20)