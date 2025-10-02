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
