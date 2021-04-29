def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    list_phrase = list(phrase)

    for index,ele in enumerate(list_phrase):
        if ele.isupper() and ele == to_swap.upper():
            list_phrase[index] = ele.lower()
        if ele.islower() and ele == to_swap.lower():
            list_phrase[index] = ele.upper()
    return (''.join(list_phrase))
 
  