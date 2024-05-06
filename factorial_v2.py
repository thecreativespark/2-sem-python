x = int(input("Enter a number:"))

def facto(num):
    if(num < 2):
        return 1
    else:
        return num*facto(num-1)

print(facto(x))
