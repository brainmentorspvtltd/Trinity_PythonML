a = 5
b = 12

#walrus operator - :=
#print("Sum is",c := a + b)

'''
c = a + b
d = a - b
e = a / b
f = a * b

print(f"Sum is {c}")
print(f"Sub is {d}")
print(f"Div is {e}")
print(f"Mul is {f}")
'''

print(f"""
Sum is {(c := a + b)}
Sub is {(d := a - b)}
Div is {(e := a / b)}
Mul is {(f := a * b)}
""")



















