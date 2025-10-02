import sys
from stats import length_of_text, get_chars_dict, sort_chars

def get_book_text(filepath):
    with open(filepath, "r") as f:
        text = f.read()
        return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")


    print("----------- Word Count ----------")
    num_words = length_of_text(text)
    print(f"Found {num_words} total words")

    print("-------- Character Count -------")
    letter_counts = get_chars_dict(text)
    sorted_chars = sort_chars(letter_counts)

    for char, count in sorted_chars:
        print(f"{char}: {count}")  

    print("============= END ===============")
main()
