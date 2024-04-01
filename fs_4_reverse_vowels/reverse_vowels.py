def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    # Extract vowels from the string
    vowel_indices = [i for i, char in enumerate(s) if char in vowels]
    # Reverse the list of vowels
    reversed_vowels = [s[i] for i in reversed(vowel_indices)]
    # Reconstruct the string with reversed vowels
    result = ''
    for i, char in enumerate(s):
        if char in vowels:
            result += reversed_vowels.pop(0)
        else:
            result += char
    return result