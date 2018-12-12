# %%prun # test init time in ipython


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_fast(n, a=1, b=1):
    if n == 1:
        return b
    else:
        return fib_fast(n-1, b, a+b)


def fib2(n):
    if n < 1:
        return 0
    elif n < 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


def fib_fast2(n, a=0, b=1):
    if n == 1:
        return b
    else:
        return fib_fast2(n-1, b, a+b)

# fib(20)
# fib_fast(20)


print("fib(10)=", fib(10), "\nfib_fast(10)=", fib_fast(10))
print("fib2(10)=", fib2(10), "\nfib_fast2(10)=", fib_fast2(10))
