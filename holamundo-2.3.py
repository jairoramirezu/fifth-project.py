#creando una función que muestre la serie fibonacci entre 0 y el numero dado

def fibonacci(num):
  a,b = 0,1
  fibonacci_lista = [0]
  for i in range(num): #este for se ejecuta desde 0 hasta el numero que le pasemos, podemos agregar otro parametro para que no comience el 0
    if b > num: return fibonacci_lista
    else:
      fibonacci_lista.append(b)
      a,b = b,a+b

resultado = fibonacci(20)
print(resultado)


