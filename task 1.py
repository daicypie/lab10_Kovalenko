def is_hidden(s1, s2):
    s2 = s2.lower()
    index = 0

    for char in s1.lower():
        index = s2.find(char, index)
        if index == -1:
            return "No"
        index += 1

    return "Yes"


s1 = input("Введіть перший рядок: ")
s2 = input("Введіть другий рядок: ")

print(is_hidden(s1, s2))
