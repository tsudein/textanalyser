import re
from collections import Counter

def count_characters(text):
    return len(text)

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    return len([s for s in sentences if s.strip()])

def most_frequent_word(text):
    words = re.findall(r'\w+', text.lower())
    most_common = Counter(words).most_common(1)
    return most_common[0] if most_common else None

def contains_phrase(text, phrase):
    return phrase in text

if __name__ == "__main__":
    user_input = input("Enter your text: ")
    print(f"Characters: {count_characters(user_input)}")
    print(f"Words: {count_words(user_input)}")
    print(f"Sentences: {count_sentences(user_input)}")
    frequent_word = most_frequent_word(user_input)
    if frequent_word:
        print(f"Most frequent word: '{frequent_word[0]}' ({frequent_word[1]} times)")
    else:
        print("No words found.")
    phrase = input("Enter a phrase to check: ")
    print(f"Contains '{phrase}': {contains_phrase(user_input, phrase)}")
