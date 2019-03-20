class Counter(object) :
    def __init__(self, fun) :
        self._fun = fun
        self.counter=0
    def __call__(self,*args, **kwargs) :
        self.counter += 1
        return self._fun(*args, **kwargs)

count = 0
def hanoi_move(n, source, dest, intermediate):
    global count
    count += 1
    if n >= 1:  # 递归出口，只剩一个盘子
        hanoi_move(n-1, source, intermediate, dest)
        print("Step %d: Move %s -> %s" % (count, source, dest))
        hanoi_move(n-1, intermediate, dest, source)

hanoi_move(3, 'source', 'dest', 'intermediate')
print(count)