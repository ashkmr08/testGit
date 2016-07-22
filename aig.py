def outter(n):
    def inner(x):
        print n*x
    return inner

y=outter(3)
print y(5)




def first(func):
    def inner(*args):
        print ('*' * 30)
        return func(*args)
    return inner


def decorator(func):
    def inner(a,b):
        print "decorator starts here"
        if(b==0):
            print "cant divide by 0"
            return
        return func(a,b)
    return inner
@first
@decorator
def divide(a,b):
      return a/b

print divide(2,2)
