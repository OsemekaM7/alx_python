def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as ne:
        print(message, ne)