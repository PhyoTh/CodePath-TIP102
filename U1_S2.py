def nanana_batman(x):
    res = ""
    count = x
    while count > 0:
        res += "na"
        count -= 1
    
    if x > 0:
        res += " "
        
    res += "batman"
    return res

# Problem 1: Transpose Matrix
def transpose(matrix):
    n = len(matrix) # row
    m = len(matrix[0]) #col
    res = [[0] * n for _ in range(m)] 
    
    for i in range(n):
        for j in range(m):
            res[j][i] = matrix[i][j]
    return res

print(transpose([[1, 2, 3], [4, 5, 6]]))

# Problem 2: Two-Pointer Reverse List
def reverse_list(lst):
    first = 0
    last = len(lst) - 1
    
    while first < last:
        temp = lst[first]
        lst[first] = lst[last]
        lst[last] = temp
        first += 1
        last -= 1
        
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
lst = []
reverse_list(lst)
print(lst)
