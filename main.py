def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

import sys

from stats import word_counter    

from stats import character_counter

from stats import dict_create

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def main():
    contents = get_book_text(book_path)
    word_count = word_counter(contents)
    character_count = character_counter(contents)
    end_count = dict_create(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("Character count")
    for item in end_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

    
    
