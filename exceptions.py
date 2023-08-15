import sys # importing this to be able to exit when error occurs
try: #this is smooth out the errors
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: value cannot be a word")
    sys.exit(1)
try: #this is to smooth the errors
    result = x/y
except ZeroDivisionError: # exception rule implented for zero division
    print("Error: cannot divide by 0.") #error statement
    sys.exit(1)#exit using status code 1 wheich means somethig went wrong
print(f"{x}/{y} = {result}")

#will have the division error for zero numbers
#need to catch the exception 