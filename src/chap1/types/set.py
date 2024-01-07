"""
集合 Set Python中的集合与JavaScript中的Set相同
"""

text = "apple banana cherry apple banana"
words = text.split(" ")
unique_words = set(words)
sorted_words = sorted(unique_words)

print(sorted_words)