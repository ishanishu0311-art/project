import random
t="------------WELCOME TO PASSWOARD SUGGESTION WINDOW-------------"
print(t.center(100))
print("-"*100)
print(" "*100)
print("!!!ALERT!!!   !!!!This application is probhited for following length of password only!!!!!!    ")
print("-"*100)
print(" "*100)
o1 = "1.length of password will be 8"
o2 = "2.length of password will be 12"
o3 = "3.length of password will be 16"
print(o1.ljust(65),end="")
print(o2.ljust(65),end='')
print(o3)
UPPERCASE_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_CHARS = "abcdefghijklmnopqrstuvwxyz"
DIGITS_1_TO_9 = "123456789" 
SPECIAL_CHARS = "$%&#@*!" 
x=int(input("please enter length of your password "))
f=''
if x>3 or x<1:
    print("please select appropriate option ")
elif x==1:
    for i in range(2):
       x=random_upper = random.choice(UPPERCASE_CHARS)
       y=random_lower = random.choice(LOWERCASE_CHARS)
       z=random_digit = random.choice(DIGITS_1_TO_9)
       w=random_symbol = random.choice(SPECIAL_CHARS)
       str(x)
       str(y)
       str(z)
       str(w)
       f=f+(x+y+w+z)
    print("password will be:    ",f)
elif x==2:
    for j in range(3):
       p=random_upper = random.choice(UPPERCASE_CHARS)
       q=random_lower = random.choice(LOWERCASE_CHARS)
       r=random_digit = random.choice(DIGITS_1_TO_9)
       s=random_symbol = random.choice(SPECIAL_CHARS)
       str(p)
       str(q)
       str(r)
       str(s)
       f=f+(p+q+r+s)
    print("password will be:    ",f)
elif x==3:
    for z in range(4):
       t=random_upper = random.choice(UPPERCASE_CHARS)
       u=random_lower = random.choice(LOWERCASE_CHARS)
       v=random_digit = random.choice(DIGITS_1_TO_9)
       w=random_symbol = random.choice(SPECIAL_CHARS)
       str(t)
       str(u)
       str(v)
       str(w)
       f=f+(t+u+v+w)
    print("password will be:     ",f)
print("-"*100)
print(" "*100)
print("~~~~~~~~~~THANK YOU FOR VISITING US~~~~~~~~~")
print("~"*100)
    


