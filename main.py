def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


from stats import word_counter    
    
                    
                       
            
                                                                                                        




def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = word_counter(contents)
    print(f"{word_count} words found in the document")


main()

    
    
