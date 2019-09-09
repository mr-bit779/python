x=100
y=345
z=700
if x<y or z>y:
    print("both condition are true")
if x<y and z>y:
    print("the conditions are true")
if not z<y:
    print("the condition is true")
a=True
print("a is",not a)
b=False
print("b is ",not b)
print(id(x),id(y),id(z))