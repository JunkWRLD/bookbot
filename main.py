from stats import num_words_func
from stats import char_count
from stats import sorted_dict_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = num_words_func(get_book_text(sys.argv[1]))
    num_chars = char_count(get_book_text(sys.argv[1]))
    sorted_dict = sorted_dict_list(char_count(get_book_text(sys.argv[1])))
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for i in sorted_dict:
        char = i["char"]
        num = i["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print(f"============= END ===============")

 #   print(f"{num_words} words found in the document")
 #   print(num_chars)

    



main()
