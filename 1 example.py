def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

def main():
    text = input("Введіть текст: ")
    if not text.strip():
        print("It's not a palindrome")
    elif is_palindrome(text):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

main()