from math import*

x = float(input("введите 1 число: "))
print ("введите операцию(+, -, *, /)")
print("Введите цифру, обозначенную для функции: 1. e^(x+y), 2. sin(x+y), 3. cos(x+y), 4. x^y)")
b = str(input())
y = float(input("введите 1 число: "))

match(b):
    case "+":
        print (x, " + ", y, " = ", x + y)
    case "-":
        print(x, " - ", y, " = ", x - y)
    case "*":
        print(x, " * ", y, " = ", x * y)
    case "/":
        print(x, " . ", y, " = ", x / y)
    case "1":
        print("e^(",x, "+", y, ")", " = ", e**(x+y))
    case "2":
        print(x, " sin(",x, "+", y, ")", " = ", sin(x + y))
    case "3":
        print(x, " cos(",x, "+", y, ")", " = ", cos(x + y))
    case "4":
        print(x, "^", y, " = ", x**y)



