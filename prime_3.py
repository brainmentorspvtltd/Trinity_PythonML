import math
#Prime Number
num = 997

if num % 2 == 0 or num % 3 == 0:
    prime = False

x = 0
for i in range(5,int(math.sqrt(num)),6):
    x += 1
    if num % i == 0 or num % i + 2 == 0:
        print("Not prime number...")
        break
else:
    print("Number is prime...")

print(f"Took {x} iterations")
