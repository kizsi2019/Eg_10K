def count_words(text):
    words = text.split()
    return len(words)

text = "This is a sample text for testing."
word_count = count_words(text)
print(word_count)  # Output: 7