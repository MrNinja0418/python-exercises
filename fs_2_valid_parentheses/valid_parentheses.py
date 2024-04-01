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

    stack = []
    for paren in parens:
        if paren == '(':
            stack.append(paren)
        elif paren == ')':
            if not stack:
                return False  # Unmatched closing parenthesis
            stack.pop()
    return len(stack) == 0  # Check if all opening parentheses have been matched