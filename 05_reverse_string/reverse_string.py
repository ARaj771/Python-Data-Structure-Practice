def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    list_phrase = list(phrase)
    reversed_list = list_phrase[::-1]
    reversed_str = "".join(reversed_list)
    return reversed_str
    
   

