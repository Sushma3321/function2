n = int(input())
div = int(input())

def FindSumOfRemainders(n, div):
    i=1
    result=0
    while i<=n:
        a=i%div
        result+=a
        i=i+1
    return result
result = FindSumOfRemainders(n, div)
print(result)