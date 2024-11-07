def input_words():
    words = []
    print("enter words and type 'done' to finish:")
    while True:
        word = input("enter a word: ")
        if word.lower() == 'done':
            break
        words.append(word)
    return words

def filter(words):
    return [word.upper() for word in words if len(word) <= 3]

def main():
    user_words = input_words()
    filtered_words = filter(user_words)
    print(filtered_words)

main()