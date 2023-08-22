def raise_exception():
    try:
        raise TypeError("This is a custom type error.")
    except TypeError as e:
        print("Exception has been raised")

# print(raise_exception());