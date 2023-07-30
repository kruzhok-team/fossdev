def fib_nohint(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

def fib_hint(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b
