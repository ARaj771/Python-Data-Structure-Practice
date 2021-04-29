def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
   

    str_num1 = str(num1)
    str_num2 = str(num2)
    if len(str_num1) != len(str_num2):
        return False
    else:
        for n in str_num1:
            if str_num1.count(n) != str_num2.count(n):
                return False
        return True
