# Uses python3
def calc_fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = calc_fib(n-1, computed) + calc_fib(n-2, computed)
    return computed[n]


n = int(input())
print(calc_fib(n))
