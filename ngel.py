def next_greatest_left(arr):
    s = []
    res = [-1] * len(arr)
    
    for i in range(len(arr)):
        while s and arr[s[-1]] < arr[i]:
            res[s.pop()] = arr[i]
        s.append(i)
    
    return res