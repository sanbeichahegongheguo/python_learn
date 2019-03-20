def fib(n):
    fib.count += 1

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib.count = 0
print(fib(5))
print(fib.count)


def move(n, a, b, c):
    move.count += 1

    if n == 1:
        print("step %d:" %move.count, a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move.count = 0
move(3, 'A', 'B', 'C')
print(move.count)