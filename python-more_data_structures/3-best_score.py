def best_score(a_dictionary):
    if len(a_dictionary) == 0:
            return None
    
    first_key = next(iter(a_dictionary))
    first_value  = a_dictionary[first_key]
    
    greater_keys = [key for key, value in a_dictionary.items() if value > first_value]
    
    if not greater_keys:
        return first_key
    
    best_key = max(greater_keys, key=lambda key: (a_dictionary[key], key))
    highest_score = a_dictionary[best_key]
    return best_key

# print (best_score({'Alex': 23, 'Ginny': 45, 'Georgina': 14}))