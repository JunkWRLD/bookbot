def num_words_func(text):
    words_as_string = text.split()
    num_words = len(words_as_string)
    return num_words
    
def char_count(text):
    char_dict = {}
    characters = text.lower()
    for i in characters:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    return char_dict

