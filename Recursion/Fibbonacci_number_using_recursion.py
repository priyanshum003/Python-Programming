# To find the Fibonacci number -  Recursion is not the best method but this code is for practise !

def fib(n):
    #Fibonacci sequence, in which each number is the sum of the two preceding ones
    if n == 1 or n == 2 :
        return  1

    fib_n_1 = fib(n-1)
    fib_n_2 = fib(n-2)

    output = fib_n_1 + fib_n_2
    return output



n = int(input())
print(fib(n))
