# 二分查找的要求是序列必须已经从小到大排好序了
def binary_search(alist, item):
    """递归版本"""
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False

def binary_search_2(alist, item):
    """非递归"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__ == '__main__':
    li = [17, 20, 21, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li, 55))
    print(binary_search(li, 155))
    print(binary_search_2(li, 55))
    print(binary_search_2(li, 155))
