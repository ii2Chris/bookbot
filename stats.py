def length_of_text(text):
    # split the text into words
    text_length = []
    for word in text.split():
        text_length.append(word)
    return len(text_length)


def get_chars_dict(text):
    # create a dictionary of characters and their counts
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    # item is a tuple (char, count)
    return item[1]

def sort_chars(chars):
    # [('a', 10), ('b', 5), ('c', 20)]
    items = list(chars.items())

    sorted_items = sorted(items, key=sort_on, reverse=True)
    return sorted_items
