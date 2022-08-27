# Define a function which takes one argument which is the limit upto which the function has to print the numbers and their label(even or odd) as shown below.

def label_series():
    i=0
    while i<=3:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
label_series()

        
