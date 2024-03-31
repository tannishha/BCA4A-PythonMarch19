#WAP to check if one No. is divisible by the other or not
print("Name:Tanisha Jain\nRoll No: 2210997251")

num = int(input("Enter a number: "))
divisor = int(input("Enter another number: "))
if num%divisor==0:
    print(num,"is divisible by",divisor)
else:
    print(num,"is not divisible by",divisor)