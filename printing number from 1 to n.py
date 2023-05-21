#printing number from 1 to n using single variable
def f(n):
    if n==0:
        return
    else:
        f(n-1)
    print(n,end=" ")
    return