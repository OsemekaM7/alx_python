import sys

def main():
    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    if num_args == 0:
        print("0 arguments")
        print(".")
    elif num_args == 1:
        print("{} argument:".format(num_args))
        for idx, arg in enumerate(args, start=1):
            print("{}: {}".format(idx, arg))
    else:
        print("{} arguments:".format(num_args))
        for idx, arg in enumerate(args, start=1):
            print("{}: {}".format(idx, arg))

if __name__ == "__main__":
    main()