def quadratic_equation(a: int, b: int, c: int):
    #a*x**2+b*x+c=0
    if a != 0:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return "the discriminant of the given equation is negative"
        elif d == 0:
            return -b / 2 * a
        else:
            x1 =((-1 * b) + (d ** 0.5)) / (2 * a)
            x2 =((-1 * b) - (d ** 0.5)) / (2 * a)
        return [x1, x2]
    else:
        return -c/b

print(quadratic_equation(1, -1, -1))