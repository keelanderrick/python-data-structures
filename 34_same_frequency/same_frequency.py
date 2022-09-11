def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dict1 = {}
    dict2 = {}

    for x in str(num1):
        dict1[x] = dict1.get(x, 0) + 1
    for x in str(num2):
        dict2[x] = dict2.get(x, 0) + 1
    if dict1 == dict2: 
        return True
    return False