import sys

def main():
    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        print("Number of argument(s): {}.".format(num_args))
        print("Arguments:")
        for idx, arg in enumerate(args, start=1):
            print("{}: {}".format(idx, arg))

if __name__ == "__main__":
    main()