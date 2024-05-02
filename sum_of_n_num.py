n = int(input("Enter the Value of N: "))
if(n<1):
    print("Enter a number greater than 0")
else:
    sum = 0
    for i in range(0,n+1):
        sum += i
    print("The sum of", n, "Natural Numbers is", sum)
