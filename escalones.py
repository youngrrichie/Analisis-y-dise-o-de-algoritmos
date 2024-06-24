#Diccionario para almacenar los datos en el caché
memo = {}
#Función para la secuencia Fibonacci
def fib(n):
  #Si n ya está en el diccionario
    if n in memo:
      return memo[n]
  #Si n es 0 devuelve 1, ya que fib de 0 es 1
    if n == 0:
      return 1
  #Si n es menos que 0 devuelve 0, ya que no hay negativos
    if n < 0:
      return 0
  #Para los demás casos hace el cálculo y lo guarda en el diccionario
    memo[n] = fib(n-1) + fib(n-2) + fib(n-3)
    return memo[n]
# Función para contar las formas de subir la escalera
def contador(n):
  return fib(n)
# Ejemplo de uso
n = 4
print("Número de formas =", contador(n))
