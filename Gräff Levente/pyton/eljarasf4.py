 


def find_shortest_word(words):
    shortest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word

def main():
    print("Enter three words:")
    words = []
    for i in range(3):
        word = input()
        words.append(word)

    shortest_word = find_shortest_word(words)
    print("The shortest word is:", shortest_word)

if __name__ == "__main__":
    main()