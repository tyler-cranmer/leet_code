
def reverse(x):
    rev = 0
    while(x > 0):
        pop = x % 10
        rev = rev * 10 + pop
        x = x // 10

    return rev
if __name__ == "__main__":
   print(reverse(-123))
#    print(2**31 - 1)
#    print(-2**32)


