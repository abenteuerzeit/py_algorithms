def linear_search(list, target):
    """
    Returns the index position of the target if found,
    else returns None
    """
    for index in range(0, len(list)):  # len() >>> constant time operation
        if list[index] == target:  # list[i] >>> constant time operation
            return index
    return None
