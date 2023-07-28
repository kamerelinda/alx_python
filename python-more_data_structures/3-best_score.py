def best_score(a_dictionary):
    if not a_dictionary:
        return None
        # Initialize variables to keep track of the best key and value
    best_key = None
    best_value = float('-inf')

    # Iterate through the dictionary
    for key, value in a_dictionary.items():
        # Check if the current value is greater than the best value found so far
        if value > best_value:
            best_key = key
            best_value = value

    return best_key
