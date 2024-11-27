import text_analyzer

def test_count_characters():
    assert text_analyzer.count_characters("Hello!") == 6

def test_count_words():
    assert text_analyzer.count_words("Hello world!") == 2

def test_count_sentences():
    assert text_analyzer.count_sentences("Hi. How are you?") == 2

def test_most_frequent_word():
    result = text_analyzer.most_frequent_word("Hello hello world")
    assert result == ("hello", 2)

def test_contains_phrase():
    assert text_analyzer.contains_phrase("Python is awesome", "Python")
