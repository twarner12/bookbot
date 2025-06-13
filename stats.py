def get_num_words(book_contents):
    return len(book_contents.split())

def get_charters_count(text):
    char_count = {}
      
    for char in text:
        if char.isalpha() and char not in char_count:
            char_count[char] = 1
        elif char in char_count:
            char_count[char] += 1 

    return char_count

def sort_char_count(char_count):
    char_num_dict =[]
    for i in char_count:
       if i.isalpha():
        char_num_dict.append({"char": i, "num": char_count[i]})
    
    char_num_dict.sort(key=lambda x: x["num"], reverse=True)
    return char_num_dict
    


