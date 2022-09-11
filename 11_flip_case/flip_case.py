def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = ""
    for x in range(0, len(phrase)):
        if phrase[x] == to_swap or phrase[x] == to_swap.swapcase():
            result += phrase[x].swapcase()
        else:
            result += phrase[x]
    return result