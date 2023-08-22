def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    except Exception as e:
        print("Inside result: None", e)
        return None
    finally:
        print("Inside result: {}".format(result) if 'result' in locals())

    return result

# Example usage
# print (safe_print_division(10, 0))