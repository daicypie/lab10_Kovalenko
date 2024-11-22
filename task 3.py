def get_valid_integer(prompt, min_value, max_value):
    while True:
        try:
            number = int(input(prompt))
            if number < min_value or number > max_value:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
            else:
                return number
        except ValueError:
            print("Error: wrong input")

min_value = 10
max_value = 100
result = get_valid_integer("Введіть ціле число: ", min_value, max_value)
print(f"Введене число: {result}")
