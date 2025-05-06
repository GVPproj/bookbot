from stats import get_word_count, get_character_count, sort_dicts
import sys

# path = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def check_argv():
    if len(sys.argv) < 2:
        return False
    else:
        pass

def main():
    if check_argv() == False:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(f"./{path}")
    char_dicts = sort_dicts(get_character_count(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")
    for dict in char_dicts:
        print(dict["char"] + ":", dict["num"])

main()
