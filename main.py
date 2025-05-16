from stats import get_word_count, get_character_counts, sorted_character_list
import sys

def get_book_text (file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    character_dict = get_character_counts(book)
    sorted_dict = sorted_character_list(character_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book)} total words")
    print("--------- Character Count -------")
    for character_dict in sorted_dict:
        print(f"{character_dict['char']}: {character_dict['num']}")
    print("============= END ===============")

main()


