def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    if (len(parens)) % 2 != 0:
        return False
    
    count = 0
   
    for p in parens:
        if p =='(':
            count = count + 1
       
 
        elif p == ')':
            count = count- 1
           
        if count < 0:
            return False
   

    return  count == 0
