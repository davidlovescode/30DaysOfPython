#quadratic equation
x = -5
y = x**2 + 6*x + 9
while y != 0:
    x += 1
    y = x**2 + 6*x + 9
    print(f"x = {x} | y = {y}")