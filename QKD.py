import cirq
import random  # Import for random basis selection

# Function to create an entangled Bell pair of qubits
def create_entangled_bell_pair():
    """Creates an entangled Bell pair of qubits."""
    qubits = cirq.LineQubit.range(2)
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),  # Apply Hadamard to the first qubit
        cirq.CNOT(qubits[0], qubits[1])  # Apply CNOT for entanglement
    )
    return circuit, qubits

# Function for Alice to randomly select a basis and measure her qubit
def alice_select_basis_and_measure(circuit, qubit):
    """Randomly selects a basis and measures Alice's qubit."""
    basis = random.randint(0, 1)  # Randomly choose basis
    if basis == 1:
        circuit.append(cirq.H(qubit))  # Apply Hadamard if basis is 1
    circuit.append(cirq.measure(qubit, key='alice_result'))
    return circuit

# Function for Bob to randomly select a basis and measure his qubit
def bob_select_basis_and_measure(circuit, qubit):
    """Randomly selects a basis and measures Bob's qubit."""
    basis = random.randint(0, 1)  # Randomly choose basis
    if basis == 1:
        circuit.append(cirq.H(qubit))  # Apply Hadamard if basis is 1
    circuit.append(cirq.measure(qubit, key='bob_result'))
    return circuit

# Simulate the QKD protocol
def simulate_qkd():
    # Step 1: Create an entangled pair
    entangled_circuit, qubits = create_entangled_bell_pair()

    # Step 2: Alice randomly selects a basis, measures, and "sends" her qubit
    entangled_circuit = alice_select_basis_and_measure(entangled_circuit, qubits[0])

    # Step 3: Bob randomly selects a basis and measures his qubit
    entangled_circuit = bob_select_basis_and_measure(entangled_circuit, qubits[1])

    # Simulate the quantum circuit
    try:
        simulator = cirq.Simulator()
        result = simulator.run(entangled_circuit, repetitions=1)
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
        return

    # Step 4: Key generation (compare bases and extract key)
    alice_key = result.measurements['alice_result'][0, 0]
    bob_key = result.measurements['bob_result'][0, 0]

    print(f"Alice's key: {alice_key}")
    print(f"Bob's key: {bob_key}")
    print('\n')
    if alice_key == bob_key:
        print("Keys match! Secure key generation successful.")
    else:
        print("Keys do not match. Possible eavesdropping.")
    print('\n')
    # Display the final quantum circuit and measurement results
    print("Final quantum circuit:")
    print(entangled_circuit)
    print('\n')
    print("Measurement results:")
    print(result)
    print('\n')
# Run the simulation
simulate_qkd()

# Function for Creating Entangled Pair:
# create_entangled_bell_pair():
# Creates two qubits.
# Applies a Hadamard gate to the first qubit, putting it in a superposition state.
# Applies a CNOT gate with the first qubit as control and the second as target, creating entanglement.
# Returns the generated quantum circuit and the two qubits.
# Functions for Basis Selection and Measurement:
# alice_select_basis_and_measure() and bob_select_basis_and_measure():
# Randomly chooses a basis (0 or 1).
# If the basis is 1, applies a Hadamard gate to the qubit to switch bases.
# Measures the qubit and stores the result using a unique key.
# Returns the updated circuit.
# Simulating the QKD Protocol:
# simulate_qkd():
# Creates an entangled pair of qubits.
# Alice randomly selects a basis, measures her qubit, and "sends" it (represented in the circuit).
# Bob randomly selects a basis and measures his qubit.
# Simulates the quantum circuit using Cirq's simulator.
# Extracts keys based on the measurements and matching bases.
# Prints the keys and whether they match (indicating successful key generation or potential eavesdropping).
# Prints the final circuit and measurement results for debugging and understanding.
# Points to note:
# This code simulates a simplified version of quantum key distribution (QKD), a secure communication method using quantum mechanics.

# It involves entanglement, basis choices, measurements, and key generation.

# It does not involve

# Further Additions:
# Error Correction and Privacy Amplification:
# In a real QKD system, error correction and privacy amplification are essential components. We can implement error correction codes (such as the repetition code) to correct errors in the key. Privacy amplification helps to distill a shorter, more secure key by hashing the raw key.

# Hashing is the process of transforming any given key or a string of characters into another value.