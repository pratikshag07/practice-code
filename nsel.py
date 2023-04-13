def next_smallest_element_left(arr):
    n = len(arr)
    res = [-1] * n
    s = []
    for i in range(n):
        while s and arr[i] < arr[s[-1]]:
            res[s.pop()] = arr[i]
        s.append(i)
    return res