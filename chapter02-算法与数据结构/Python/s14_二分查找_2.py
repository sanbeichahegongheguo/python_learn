"""
python，不能忽视其强大的标准库。经查阅，发现标准库中就有一个模块，名为：bisect。
其文档中有这样一句话：

This module provides support for maintaining a list in sorted order without 
having to sort the list after each insertion. 
For long lists of items with expensive comparison operations, 
this can be an improvement over the more common approach. 
The module is called bisect because it uses a basic bisection algorithm 
to do its work. 
The source code may be most useful as a working example of 
the algorithm (the boundary conditions are already right!).
"""

from bisect import *

def bisectSearch(lst, x):          
    i = bisect_left(lst, x)         #bisect_left(lst,x)，得到x在已经排序的lst中的位置
    if i != len(lst) and lst[i] == x:
        return i
    raise ValueError

if __name__=="__main__":
    lst = sorted([2,5,3,8])
    print(bisectSearch(lst,5))
