def duplicate_encode(word="Ffdgh(( @"):
    new_str = ""
    for symbol in word.lower():
        if word.lower().count(symbol) == 1:
            new_str += "("
        elif word.lower().count(symbol) > 1:
            new_str += ")"
        # print(new_str)
    # print(new_str)

    return new_str




duplicate_encode()