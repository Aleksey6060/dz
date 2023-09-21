import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на 0"
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Ошибка: невозможно извлечь квадратный корень из отрицательного числа"
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Ошибка: невозможно вычислить факториал отрицательного числа"
    elif x == 0:
        return 1
    else:
        return x * factorial(x-1)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

print("Выберите операцию.")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Квадратный корень")
print("7. Факториал")
print("8. Синус")
print("9. Косинус")
print("10. Тангенс")

while True:
    try:
        choice = int(input("Введите номер операции (1-10): "))
        if choice < 1 or choice > 10:
            print("Некорректный ввод. Попробуйте еще раз.")
            continue
        break
    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")

while True:
    try:
        num1 = float(input("Введите первое число: "))
        break
    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")

if choice != 6 and choice != 7 and choice != 8 and choice != 9 and choice != 10:
    while True:
        try:
            num2 = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")

if choice == 1:
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == 2:
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 3:
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == 4:
    print(num1,"/",num2,"=", divide(num1,num2))

elif choice == 5:
    print(num1,"^",num2,"=", power(num1,num2))

elif choice == 6:
    print("√",num1,"=", square_root(num1))

elif choice == 7:
    print(num1,"! =", factorial(num1))

elif choice == 8:
    print("sin(",num1,") =", sin(num1))

elif choice == 9:
    print("cos(",num1,") =", cos(num1))

elif choice == 10:
    print("tan(",num1,") =", tan(num1))
