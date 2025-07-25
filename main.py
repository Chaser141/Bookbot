def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


from stats import word_counter    

from stats import character_counter

from stats import dict_create

def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = word_counter(contents)
    character_count = character_counter(contents)
    end_count = dict_create(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("Character count")
    for item in end_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

    
    
