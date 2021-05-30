from datetime import datetime

def my_decorator(func):
    def decor(name):
        now = datetime.now()
        print(now)
        func(name)
    return decor

def my_func(name):
    now = datetime.now()
    print(f"Hi {name}.This is the exact datetime, when you run this code.")
    # print(now.hour)
    if now.hour > 10:
        print("It's perfect time for coding!")
    else:
        print("It's probably too late,go to sleep.")

my_dec_func = my_decorator(my_func)
name = input("Input your name: ")
my_dec_func(name)