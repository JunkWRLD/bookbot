from stats import num_words_func
from stats import char_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    num_words = num_words_func(get_book_text("books/frankenstein.txt"))
    num_chars = char_count(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(num_chars)

main()
