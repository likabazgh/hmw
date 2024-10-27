def count_vowels(text):
    text.lower()
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text1 = input("enter text: ")
text2 = input("enter text: ")
text3 = input("enter text: ")

print(count_vowels(text1))
print(count_vowels(text2))
print(count_vowels(text3))