def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Ділення на нуль!")
    else:
        return result

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
result = divide(num1, num2)
if result:
    print("Результат:", result)