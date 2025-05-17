# metod fibonacci
def fibonacci(n):
    # inicia com 0 e 1
    fib = [0, 1]

    #roda ate encontrar o n, ate o utimo numero fib[-1] for menor ou igual a n
    while fib[-1] < n:

        #vai gerando os proximos numeros da sequencia
        fib.append(fib[-1] + fib[-2])
        
    # quando o último número da sequência for maior ou igual a n, ele retorna
    return fib

# entrada
numero = int(input("Digite um número para verificar se ele está na sequência de Fibonacci: "))

# o fibon vai receber o dado de entrada
sequencia_fib = fibonacci(numero)

if numero in sequencia_fib:
    print(f"O número {numero} pertence à sequência de Fibonacci.")

else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
