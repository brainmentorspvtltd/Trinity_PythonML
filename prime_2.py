#Prime Number
num = 17
x = 0
for i in range(2,num//2):
    x += 1
    if num % i == 0:
        print("Not prime number...")
        break
else:
    print("Number is prime...")

print(f"Took {x} iterations")
