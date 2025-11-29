print("half piramid right angle triangle made with (*):")
n=int(input("enter the number of rows"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()