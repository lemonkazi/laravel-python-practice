def greet():
    print("Hello, welcome to Python!")

greet()


#range(start, stop, step)
for i in range(1, 6):     # 1 to 5
    print(i)

for i in range(10, 0, -2): # 10, 8, 6, ...
    print(i)


def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))  # 10

def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show(name="Lemon", age=30)
