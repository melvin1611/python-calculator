a=int(input('enter 1st number'))
b=int(input('enter the second element'))
print('1. Addition')
print('2. Substraction')
print('3. multiplication')
print('4. division')
choice=int(input('enter ur choice'))
if choice==1:
  print(a+b)
elif choice==2:
  print(a-b)
elif choice==3:
  print(a*b)
else choice==4:
    if b!=0:
      print(a/b)
    else b=0:
      print('not defined')
