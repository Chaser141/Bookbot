def word_counter(contents):
    words = contents.lower().split()
    return len(words)



def character_counter(contents):
    low_words = contents.lower()
    count = {}
    for char in low_words:
        count[char] = count.get(char, 0) + 1
    return count


def dict_create(count):
    final_count = []
    for char, num in count.items():
        if char.isalpha():
            new_dict = {"char": char, "num": num}
            final_count.append(new_dict)
    final_count.sort(reverse=True, key=sort_on)
    return final_count   

def sort_on(items):
    return items["num"]
    
