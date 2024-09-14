def fact(n):
    f=1
    for i in range(1, n+1):
        f*=i
    return f
t = fact(5)
print(t)
if __name__ == '__main__':
    print("------------------testing code ------ ")
    print(fact(4))
    print(fact(7))
    print(" ---------------------------------------  ")