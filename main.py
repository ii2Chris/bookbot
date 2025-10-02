from stats import length_of_text, get_chars_dict

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = length_of_text(text)
    print(f"Found {num_words} total words")


    letter_counts = get_chars_dict(text)
    print(f"Found {len(letter_counts)} total words")
    print(letter_counts)    

main()
