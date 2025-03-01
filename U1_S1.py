def linear_search(lst, target):
    res = []
    for i, x in enumerate(lst):
        if x == target: res.append(i)
        return res