def lab01():
    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x <= 4:
        y = (pow(a,2)/pow(x,2)) + 6*x
    else:
        if x > 4:
            y = pow(b,2)*pow((4+x),2)

    print("y = %.1f" % y)


if __name__ == '__main__':
    lab01()