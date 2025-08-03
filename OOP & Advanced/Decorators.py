def logger(func):
    def wrapper():
        print("Before....")
        func()
        print("After...")

    return wrapper


@logger
def greet():
    print("Hello")


greet()
#-----------------------
