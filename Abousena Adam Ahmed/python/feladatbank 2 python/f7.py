def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

text = "rgagtadfqw"
num_words = word_count(text)
print(num_words)  # Output: 7