def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_list_of_chars(chars_dict):
    new_list = []
    for char, num in chars_dict.items():
        dict_item = {"char": char, "num": num}
        new_list.append(dict_item)
    new_list.sort(reverse=True, key=sort_on_num)
    return new_list
                      
def sort_on_num(item):
    return item["num"]