class Counter(object) :
    def __init__(self, fun) :
        self._fun = fun
        self.counter=0
    def __call__(self,*args, **kwargs) :
        self.counter += 1
        return self._fun(*args, **kwargs)

# 斐波那契数列
@Counter
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5)) # 5
print(fib.counter) # 15

# 汉诺塔问题
@Counter
def move(n, a, b, c):
    if n == 1:
        print("step %d:" %move.counter, a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')
print(move.counter) # 10