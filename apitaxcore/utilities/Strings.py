def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
