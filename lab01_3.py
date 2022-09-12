class Class:
    def __init__(self,x):
        self.x =x
    def lab01(self):

        try:  # Защищенный блок 1
            a = float(input("Введите A= "))
            y = (pow(a, 2) / pow(x1, 2)) + 6 * x1
        except:  # Обработчик ошибок для защищенного блока 1
            print("На ноль делить нельзя!")
        print("y = %.1f" % y)

    def lab01_2(self):
            b = float(input("Введите B= "))
            y = pow(b, 2) * pow((4 + x1), 2)
            print("y = %.1f" % y)

if __name__ == '__main__':
    while True:
        x1 = float(input("Введите X "))
        if x1 <=4:
            up = Class(x1)
            up.lab01()
        elif x1 > 4:
            up = Class(x1)
            up.lab01_2()