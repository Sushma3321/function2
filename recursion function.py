
def my_function(num):
    sum=0
    tem=num
    while num>0:
        tem=num%10
        num=num//10
        sum=sum+tem
        return sum*my_function(sum+1)
    print(sum)
    if sum%2==0:
        print("even")
    else:
        print("odd")
my_function(3467)
    
# def counter(c):3
#     if c==1:
#         return c
#     else:
#         return c*counter(c-1)
# print(counter(5))



    