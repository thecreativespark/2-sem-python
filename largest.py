a = int(input("Enter the number a = "))
b = int(input("Enter the number b = "))
c = int(input("Enter the number c = "))

def largoftwo(a,b):
    if a>b:
        return a
    else:
        return b

temp = largoftwo(a,b)
if largoftwo(temp,c)==a:
    print("a =", a, "is the greatest.")
elif largoftwo(temp,c)==b:
    print("b =", b, "is the greatest.")
else:
    print("c =", c, "is the greatest.")
