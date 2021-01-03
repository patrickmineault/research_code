memory = {}

def fib(n):
    global memory
    if n not in memory:
        if n >= 2:
            memory[n] = fib(n-2) + fib(n-1)
        else:
            memory[n] = 1
    return memory[n]