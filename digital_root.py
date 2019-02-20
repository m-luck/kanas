def digital_root(n):
    string = str(n)
    chars = list(string)
    print(chars)
    sigma = 0
    for digit in chars:
        sigma += int(digit)
    if len(str(sigma)) > 1:
        sigma = digital_root(sigma)
    return sigma
