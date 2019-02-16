def unique_in_order(iterable):
    old_char = None
    unique = []
    for char in iterable:
        if char != old_char:
            unique.append(char)
        old_char = char
    return unique
            
