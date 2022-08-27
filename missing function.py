# def missing(a):
#     b=list(range(a[0],a[-1]+1))
#     i=0
#     c=[]
#     while i<=len(a):
#         if b[i] not in a:
#             c.append(b[i])
#         i=i+1
#     print(c)
# missing([1,3,5,6,8,9])



def missing(a):
    i=1
    b=[]
    while i<len(a):
        if i not in a:
            b.append(i)
        i=i+1
    print(b)
missing([1,3,5,6,8,9])
        
            

