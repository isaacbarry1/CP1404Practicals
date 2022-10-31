"""
Word Occurrences
Estimate: 25minutes
Actual: 30 minutes
"""

text = input("Text: ")

word_to_count = {}

words = text.split()

for word in words:
    occurrence = word_to_count.get(word, 0)
    word_to_count[word] = occurrence + 1

words = list(word_to_count.keys())
words.sort()

# Took this part from solutions, didn't know how to do it
length = max((len(word) for word in words))
for word in words:
    print(f"{word:{length}} = {word_to_count[word]}")

