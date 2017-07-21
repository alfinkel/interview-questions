def validate_closure(seq):
    """
    Check that a string sequence is valid when using {}, [], ().
    
    For example:
        > validate_closure('al{fi[nk]el}(st{e}in)') will return True
        > validate_closure('()') will return True
        > validate_closure('al{fi[nkel}](st{e}in)') will return False
        > validate_closure('(') will return False
        > validate_closure(']') will return False
    """
    match = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for character in seq[:]:
        if character in match.keys():
            stack.append(character)
        if character in match.values():
            if not stack:
                return False
            last = stack.pop()
            if match[last] != character:
                return False
    if stack:
        return False
    return True
