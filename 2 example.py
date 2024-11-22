text1 = input("Введіть перше слово: ")
text2 = input("Введіть друге слово: ")

text1_processed = text1.replace(" ", "").lower()
text2_processed = text2.replace(" ", "").lower()

if text1_processed == "" and text2_processed == "":
    print("Не анаграми")
else:
    if sorted(text1_processed) == sorted(text2_processed):
        print("Анаграми")
    else:
        print("Не анаграми")