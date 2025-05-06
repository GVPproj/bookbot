def get_word_count(text):
    num = len(text.split())
    return num

def get_character_count(text):
    char_count = {}
    words = text.split()
    for word in words:
        chars = list(word)
        for char in chars:
            clean_char = char.lower()
            if clean_char.isalpha():
                if clean_char in char_count:
                    char_count[clean_char] += 1
                else:
                    char_count[clean_char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]


def sort_dicts(dicts):
    sorted = []
    for dict in dicts:
        sorted.append({"char": dict, "num": dicts[dict]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted