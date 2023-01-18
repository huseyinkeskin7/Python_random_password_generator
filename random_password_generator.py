import random
print('Please choice your password type!')
print('1. Only letters')
print('2. Only numbers')
print('3. Letters and numbers')
choice=int(input('Your choice: '))
len = int(input("Enter the length of password:\n---------->"))
if choice==1:
    s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password =  "".join(random.sample(s,len))
    print(password)
elif choice==2:
    s="1234567890123456789012345678901234567890"
    password =  "".join(random.sample(s,len))
    print(password)
elif choice==3:
    s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password =  "".join(random.sample(s,len))
    print(password)
else:
    print("Invalid choice!")
    