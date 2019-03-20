
def combinations(lists, k):
    n = len(lists)  # 7
    result = []
    for j in range(n-k+1):
        if k > 1:
            newlists = lists[j+1:]

        result.append(lists[j])
    print(result)


if __name__ == "__main__":
    lists = ['豆奶', '草莓', '尿布', '啤酒', '辣椒酱', '黄瓜', '饼干']
    combinations(lists, 2)
