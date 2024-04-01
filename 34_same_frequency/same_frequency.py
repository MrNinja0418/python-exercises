def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # Convert numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Count the occurrences of each digit in both numbers
    count1 = {digit: str_num1.count(digit) for digit in str_num1}
    count2 = {digit: str_num2.count(digit) for digit in str_num2}
    
    # Compare the counts
    return count1 == count2