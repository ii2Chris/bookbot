def length_of_text(text):
    text_length = []
    for word in text.split():
        text_length.append(word)
    return len(text_length)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    return item[1]

def sort_chars(chars):
    items = list(chars.items())
    
    sorted_items = sorted(items, key=sort_on, reverse=True)
    return sorted_items
