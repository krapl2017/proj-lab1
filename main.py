import re

def badInput():
    print("Некорректный ввод")

correctInput = False
while (not correctInput):
    print("Введите приближённое число (оно не может равняться нулю): ")
    pattern = r'^-?\d*[.,]?\d+$'
    strN = input()
    if re.match(pattern, strN):
        numWithNoComma = strN.replace(",", ".")
        n = abs(float(numWithNoComma))
        if n == 0:
            badInput()
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
                    correctEImput = False
                    while(not correctEImput):
                        print("Введите абсолютную предельную погрешность:")
                        strE = input()
                        if re.match(pattern, strE):
                            eWithNoComma = strE.replace(",", ".")
                            e = abs(float(eWithNoComma))
                            print("Исходное приближённое число:", n)
                            print("Абсолютная погрешность:", e)
                            print("Относительная погрешность в процентах:", e / n * 100)
                            correctEImput = True
                        else:
                            badInput
                    
                elif choice == 2:
                    correctChoice = True
                    correctEImput = False
                    while(not correctEImput):
                        print("Введите относительную предельную погрешность (в процентах от 0 до 100):")
                        strE = input()
                        if re.match(pattern, strE):
                            eWithNoComma = strE.replace(",", ".")
                            e = abs(float(eWithNoComma))
                            if ( e < 100.0):
                                print("Исходное приближённое число:", n)
                                print("Относительная погрешность:", e)
                                print("Абсолютная погрешность:", e * n / 100)
                                correctEImput = True
                            else:
                                print("Некорректный ввод. Относительная погрешность должна быть меньше 100%")
                        else:
                            badInput
                else:
                    badInput
    else:
        badInput