m=int(input("enter the rows of star: "))
for i in range(1,m+1):

    if i < m//2+2:
        for k in range(1,m//2+2-i):
            print(" ",end="")
        for j in range(1, (2*i)):
            print('#',end="")
        print("\n",end="")
    else:
        for k in range(1, (i-m // 2 )):
            print(" ", end="")
        for j in range(1, (2 * m+1-2*i+1)):
            print('#', end="")
        print("\n",end="")
