def quick_sort(alist):
    if len(alist) < 2:
        return alist
    else:
        pivot = alist[0]
        less = [i for i in alist[1:] if i <= pivot] # <= 的判断在这里
        greater = [i for i in alist[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 21, 44, 55, 20]
    print(li)
    nlist = quick_sort(li)
    print(nlist)
