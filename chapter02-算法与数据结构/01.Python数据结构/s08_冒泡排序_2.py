def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1, 0, -1):
        for i in range(0, j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 21, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)
