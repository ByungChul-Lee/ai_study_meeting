def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)

n = 7
fList=[]
for i  in range(1,n+1):
    fList.append(fib(i))
    
print(fList)