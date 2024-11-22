def calculate_life_number(birthdate):
    birthdate = ''.join(filter(str.isdigit, birthdate))
    digits = [int(digit) for digit in birthdate]

    while len(digits) > 1:
        digits = [sum(digits)]

    return digits[0]

while True:
    try:
        birthdate = input("Введіть свою дату народження (РРРГММДД, РРРРДДММ або ММДДРРРР): ")
        if not birthdate.isdigit():
            raise ValueError("Введені дані повинні містити лише цифри.")
        life_number = calculate_life_number(birthdate)
        print("Ваша цифра життя:", life_number)
        break
    except ValueError as e:
        print(e)
        print("Спробуйте ще раз.")

