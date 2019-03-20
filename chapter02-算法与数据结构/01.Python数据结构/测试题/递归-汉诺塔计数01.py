count = 0 # 添加1
def fib(n):
    global count # 添加2
    count += 1 # 添加3

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5)) # 5
print(count) # 15

m = 0
def move(n, a, b, c):
    global m
    m += 1

    if n == 1:
        print("step %d:" %m, a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(3, 'A', 'B', 'C')
print(m)


