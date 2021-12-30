
def print_n_1(n):
    if n == 0 :
        return
    print(n)    #print n first and then call function for (n-1)
    print_n_1(n-1)



n = int(input())
print(print_n_1(n))
