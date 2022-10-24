def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Memoize fib function.
def fib_m(n, memoize):
    if memoize[n] is not None:
        return memoize[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_m(n-1, memoize) + fib_m(n-2, memoize)
    memoize[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n+1)
    return fib_m(n, memo)

#Bottom up approach:
# no recursion, super fast.
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[i]
    # if n == 1 or n == 2:
    #     return 1
    # bottom_up = [None] * (n)
    # bottom_up[0] = 1
    # bottom_up[1] = 1
    # for i in range(2, n):
    #     bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    # return bottom_up[i]


if __name__ == '__main__':
    print(fib(35))
    print(fib_memo(35))
    print(fib_bottom_up(35))