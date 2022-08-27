# multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])

def list_change(list1,list2):
    i=0
    b=[]
    while i<len(list1):
        a=list1[i]*list2[i]
        b.append(a)
        i=i+1
    print(b)
list_change([5,10,50,20],[2,20,3,5])


    