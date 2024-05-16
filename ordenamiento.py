import numpy as np
import time

start_time = time.time()
n = 100
array = np.random.randint(0, 100, size=n)
sorted_array = np.sort(array)
print(sorted_array)
print("Tiempo de ejecución:", time.time() - start_time, "segundos.")