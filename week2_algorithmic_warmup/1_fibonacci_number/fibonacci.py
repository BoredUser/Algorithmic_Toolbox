# Uses python3
def calc_fib(n):
    fib = [0,1]
    for i in range(n+1):
        if i>1:
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

n = int(input())
print(calc_fib(n))
