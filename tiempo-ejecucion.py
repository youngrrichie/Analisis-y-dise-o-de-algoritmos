import numpy as np
import time

# Creación de Arreglos
start_time = time.time()
A = np.random.randint(0, 100, size=100)
B = np.random.randint(0, 100, size=100)
print("Tiempo para crear los arreglos:", time.time() - start_time,
"segundos.")

# Elementos a buscar en algoritmos 1 a 3
T = np.random.choice(A)
X = np.random.choice(np.concatenate((A, B))) # Elemento de A o B
Y = np.random.choice(np.intersect1d(A, B)) # Elemento de A y B

# Algortimo 1
start_time = time.time()
print(f"Buscando {T} en A:")
if T in A:
    print(f"{T} se encuentra en A.")
else:
    print(f"{T} no se encuentra en A.")
print("tiempo de ejecución:", time.time() - start_time, "segundos.")

# Algoritmo 2
start_time = time.time()
print(f"\nBuscando {X} en A o B:")
if X in A or X in B:
    print(f"{X} Se encuentra en A o B.")
else:
    print(f"{X} No se encuentra en A ni en B.")
print("Tiempo de ejecución:", time.time() - start_time, "segundos.")

# Algoritmo 3
start_time = time.time()
print(f"\nBuscando {Y} en A y B:")
if Y in A and Y in B:
    print(f"{Y} Se encuentra en A y en B.")
else:
    print(f"{Y} No se necuentra en A y en B.")
print("Tiempo de ejecución:", time.time() - start_time, "segundos.")

# Algoritmo 4
start_time = time.time()
unique_elements, counts = np.unique(A, return_counts=True)
duplicates = unique_elements[counts > 1]
if len(duplicates) > 0:
    print(f"\nEl arreglo contiene los siguientes duplicados: {duplicates}")
else:
    print("\nEl arreglo no contiene duplicados.")
print("Tiempo de ejecución:", time.time() - start_time, "segundos.")
