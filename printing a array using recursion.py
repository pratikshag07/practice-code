##printing a array using recursion
a=[1,2,3,4,5]
n=len(a)
def f(a,i):
    if i>=n:
        return
    else:
        print(a[i],end= " ")
        f(a,i+1)
f(a,0)