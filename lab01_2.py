def lab01():
    try:  # Защищенный блок 1
        a = float(input("Введите A="))
        b = float(input("Введите B="))
        x = float(input("Введите X="))
        try:  # Защищенный блок 2
            if x <= 4:
                 y = (pow(a, 2) / pow(x, 2)) + 6 * x
            else:
                if x > 4:
                 y = pow(b, 2) * pow((4 + x), 2)
            print("y = %.1f" % y)

        except:  # Обработчик ошибок для защищенного блока 1
            print("На ноль делить нельзя!")
    except:
        print("Неверные входные данные!")
        input("Нажмите Enter для выхода")  # Задержка перед выходом из программы

if __name__ == '__main__':

    lab01()