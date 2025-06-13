import sys
from stats import ( get_num_words,
    get_charters_count,
    sort_char_count,
)

def main():
    if not len(sys.argv) > 1:

        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_contents = get_book_text(sys.argv[1])

        num_words = get_num_words(file_contents)
    
        characters_count = get_charters_count(file_contents.lower())

        sorted_char_count = sort_char_count(characters_count)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_info in sorted_char_count:
            print(f"{char_info['char']}: {char_info['num']}")
        print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents



main() 