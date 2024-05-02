a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

def largoftwo(a,b):
    if a>b:
        return a
    else:
        return b

temp1, temp2 = a, b
p = largoftwo(a,b)

if p==a:
    q = b
else:
    q = a

while(p != 0):
    p = p%q

print("GCD is", q)
