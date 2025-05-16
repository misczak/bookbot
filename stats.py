def get_word_count (text):
    text_list = text.split()
    return len(text_list)

def get_character_counts (text):
    counts = {}
    for character in text:
        character = character.lower()
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    
    return counts

def sorted_character_list (dict):
    dict_list = []
    for item in dict:
        if item.isalpha():
            dict_list.append({"char": item, "num": dict[item]})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def sort_on(dict):
    return dict["num"]