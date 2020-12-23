def fib(num: int, acc):
    if num == 0:
        return acc 
    else:
        return fib(num-1, acc + num )

print(fib(10, 0))


def this(that: int):
    print("this and that is going to be crazy")

def func(num: int ):
    if num % 2 == 0:
        return True
    else:
        return False

print(func(10))