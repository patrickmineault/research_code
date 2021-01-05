memory = {}

"""
The N'th Fibonacci number is 

F(n) = F(n-1) + F(n-2)

with F(0) = 1, F(1) = 1
"""

def fib(n):
    global memory
    if n not in memory:
        if n >= 2:
            memory[n] = fib(n-2) + fib(n-1)
        else:
            memory[n] = 1
    return memory[n]