
def powerOfN(x,n):
    if n == 0 :
        return 1

    return x * powerOfN(x,n-1)

x,n = input().split()

x = int(x)
n = int(n)

print(powerOfN(x,n))