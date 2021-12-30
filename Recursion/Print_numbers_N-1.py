
def print_n_1(n):
    if n == 0 :
        return
    print(n)    #the only difference between ptinting 1 till n and n till 1 is that we are printing n
    print_n_1(n-1)



n = int(input())
print(print_n_1(n))
