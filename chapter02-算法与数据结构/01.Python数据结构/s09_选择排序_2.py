def findSmallest(alist):
    smallest = alist[0]
    smallest_index = 0
    n = len(alist)
    for i in range(1, n):
        if alist[i] < smallest:
            smallest = alist[i]
            smallest_index = i
    return smallest_index

def select_sort(alist):
    newlist = []
    for i in range(len(alist)):
        smallest = findSmallest(alist)
        newlist.append(alist.pop(smallest))
    return newlist

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 21, 44, 55, 20]
    print(li)
    nlist = select_sort(li)
    print(nlist)
