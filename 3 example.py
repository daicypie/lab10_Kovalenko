def calculate_life_number(birthdate):

  birthdate = ''.join(filter(str.isdigit, birthdate))

  digits = [int(digit) for digit in birthdate]

  while len(digits) > 1:
    digits = [sum(digits)]

  return digits[0]

birthdate = input("Введіть свою дату народження (РРРГММДД, РРРРДДММ або ММДДРРРР): ")

life_number = calculate_life_number(birthdate)
print("Ваша цифра життя:", life_number)