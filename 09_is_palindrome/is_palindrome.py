def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_lower = phrase.lower()
  
    phrase_no_space = phrase_lower.replace(" ","")
   
    phrase_list = list(phrase_no_space)
    
    phrase_list_reversed = phrase_list[::-1]
   
    if phrase_list == phrase_list_reversed:
        return True
    else:
        return False

