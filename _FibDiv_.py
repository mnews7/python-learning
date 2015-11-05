__author__ = 'Matthew'

# Prints out a list of fibonnaci numbers divisible by numbers less than the current Fibonnaci Number 
# between 0 and n

def fib(n):

    print('Starting!')
    result = []

    a = 0
    b = 1
    # c = 0
    while a < n:
        result.append(a)
        a, b = b, a + b

    size = len(result)
    for num in range(0, size):
        divis = (division(result[num], n))
        print('Fibonacci number', result[num], 'is divisible by', divis)
    print('There are no more Fibonacci numbers between', n, 'and', result[num])
    print('All done!')


def division(reslist, n):
    divi = []

    for div in range(2, n):
        if reslist <= div:
            break
        else:
            if reslist % div == 0:
                divi.append(div)
    return (divi)


# Calling the scripts
f100 = fib(10000000000)
print(f100)
