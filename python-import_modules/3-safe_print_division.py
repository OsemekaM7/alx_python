def safe_print_division(a, b):
    if b == 0:
        if a == 0:
            print("Result: Indeterminate (0 / 0)")
        else:
            print("Inside result: None")
        return None
    else:
        result = a / b
        print("Inside result:", result)
        return result

# Example usage
# result = safe_print_division(10, 0)
# if result is not None:
#     print("Result:", result)