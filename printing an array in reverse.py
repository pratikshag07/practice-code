#printing an array in reverse using recursion
def f(a,i):
    if i<0:
       return
    else:
        print(a[i],end= " ")
        f(a,i-1)        
f(a,n-1)