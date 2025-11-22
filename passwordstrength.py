print("PASSWORD STRENGTH CHECK")
print()
passw = input("Enter your password:")
x=0   #password strengh point
remark=[]

if len(passw)>=8:
    x+=1
else:
    remark.append("Your password should have atleast 8 characters")

upper= False
for i in passw:
    if i>='A'and i<= 'Z':
        upper = True
        break
if upper:
    x+=1
else:
    remark.append("Add capital letters")

lower=False
for i in passw:
    if i >= 'a' and i <= 'z':
        lower = True
        break

if lower:
    x+=1
else:
    remark.append("Add lowercase letters")

num = False
for i in passw:
    if i >= '0' and i <= '9':
        num = True
        break

if num:
    x+= 1
else:
    remark.append("add numbers.")


spcl = False
ch = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"

for i in passw:
    if i in ch:
        spcl = True
        break

if spcl:
    x += 1
else:
    remark.append("Add special characters.")


print("Password strength:")

if x<=2:
    print("-weak")
elif x==3:
    print("-Medium")
else:
    print("-Strong")

if len(remark) == 0:
    print("No changes are required in your password")
else:
    print("suggestions to improve your password-")
    for i in remark:
        print(i)
    
