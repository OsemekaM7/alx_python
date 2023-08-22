def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
    print(result)

# Example usage
# result = safe_print_division(10, 2)
# if result is not None:
#     print("Result:", result)