# def check_number(a,b):
#     if a%2==0 and b%2==0:
#         print("both are even numbers")
#     else:
#         print("both are not same")
# check_number(2,7)

# If you call your function [2, 6, 18, 10, 3, 75] and [6, 19, 24, 12, 3, 87] then it should give this output:

def check_number_list(list1,list2):
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print("both are even")
        else:
            print("both are not same")
        i=i+1
check_number_list([2,6,18,10,3,75],[6,19,24,12,3,87])
