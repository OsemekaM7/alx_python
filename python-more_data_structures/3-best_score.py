def best_score(a_dictionary):
    if not a_dictionary:
            return None
    
    first_key = next(iter(a_dictionary))
    first_value  = a_dictionary[first_key]
    
    greater_keys = [key for key, value in a_dictionary.items() if value is not None and (first_value is None or value > first_value)]
    
    if not greater_keys:
        return first_key
    
    best_key = max(greater_keys)
    highest_score = a_dictionary[best_key]
    return best_key

# print (best_score({'Alex': None, 'Ginny': 45, 'Georgina': 14}))