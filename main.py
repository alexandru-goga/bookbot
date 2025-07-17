from stats import get_num_words, get_chars_dict, get_sorted_list_of_chars
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = get_sorted_list_of_chars(chars_dict)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for x in sorted_chars:
        if x['char'].isalpha():
            print(f"{x['char']}: {x['num']}")
    print(f"============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
