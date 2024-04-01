def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_phrase = ''
    for char in phrase:
        if char.lower() == to_swap.lower():
            swapped_phrase += char.swapcase()
        else:
            swapped_phrase += char
    return swapped_phrase
