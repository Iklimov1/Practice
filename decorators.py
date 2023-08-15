def announce(f):
    #will return modified function
    #because they are wrapped in one another its called a wrapper function
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper
@announce #adds the announce decorator to hello
def hello():
    print("Hello, World!")
hello()#running the function