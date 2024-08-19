# Maths weird problem *This loop will never end*

num = int(input("Enter the Natural Number: "))
while num > 0:
  if num%2==0:
    num = num/2
  else:
    num = num*3+1
print(num)

# Firoziyash