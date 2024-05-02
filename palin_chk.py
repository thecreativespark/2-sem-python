x = int(input("Enter a number:"))

def palinchk(num):
    temp = num
    r = 2
    rev = 0
    while(num > 1):
        r = num%10
        rev = (rev*10) + r
        num //= 10
    print("Reversed Number is:", rev)
    if rev==temp:
        print("It is a Palindrome")
    else:
        print("Not a Palindrome")

palinchk(x)
