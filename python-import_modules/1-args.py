import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name from the arguments

    num_args = len(argv)
    if num_args == 0:
        print("0 arguments")
        print(".")
    else:
        print("{} arguments".format(num_args))
        if num_args == 1:
            print("Argument:")
        else:
            print("Arguments:")
        
        for i, arg in enumerate(argv, start=1):
            print('{}: {}'.format(i, arg))

if __name__ == "__main__":
    main()
