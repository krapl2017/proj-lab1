import re
correctInput = False
while (not correctInput):
    print("Введите приближённое число (оно не может равняться нулю): ")
    pattern = r'^-?\d*[.,]?\d+$'
    strN = input()
    if re.match(pattern, strN):
        numWithNoComma = strN.replace(",", ".")
        n = float(numWithNoComma)
        if n == 0:
            print("Некорректный ввод")
        else:
            correctInput = True

            correctChoice = False
            while (not correctChoice):

                print("Выберите тип предельной погрешности:")
                print("1) абсолютная")
                print("2) относительная")
                choice = int(input())

                if choice == 1:
                    correctChoice = True
                    print("Введите абсолютную предельную погрешность:")
                    e = float(input())
                    print("Исходное приближённое число:", n)
                    print("Абсолютная погрешность:", e)
                    print("Относительная погрешность:", e / n)
                    
                elif choice == 2:
                    correctChoice = True
                    print("Введите относительную предельную погрешность:")
                    e = float(input())
                    print("Исходное приближённое число:", n)
                    print("Относительная погрешность:", e)
                    print("Абсолютная погрешность:", e * n)
                    
                else:
                    print("Некорректный ввод")
    else:
        print("Некорректный ввод")