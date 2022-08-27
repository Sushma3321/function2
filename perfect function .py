# Perfect Number?
# A perfect number is the one which is equal to the sum of all it's factors(including 1 and excluding itself).

# Define a function named perfect() which takes one argument(integer) and checks if it is a perfect number or not. Now use this code to write a program that prints all the perfect numbers between 1-1000. 



def check_perfect(n):
    i=1
    c=0
    while i<n:
        if n%i==0 :
            c=c+i
        i=i+1
    return c
n=int(input("enter the number"))
s=check_perfect(n)
if n==s:
    print("perfect")
else:
    print("not perfect")


