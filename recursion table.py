import sys
sys.setrecursionlimit(10)
print(sys.getrecursion())
i=1
def table(n):
    global i
    if n<=0:
        return n
    else:
        return i*table(n)
    i=i+1
    global i
    i=i+1
    print(n,"*",i,"=",n*i)
    table()

print(table(5))