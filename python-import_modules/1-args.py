if __name__ == "__main__":
    import sys

    argv = ["Hello", "Holberton", "School", 98, "Battery", "street"]

    num_arguments = len(sys.argv) - 1
    print("Number of argument(s): {}".format(num_arguments), end="")
    
    if num_arguments == 1:
        print(f", followed by:\n1: {sys.argv[1]}")
    elif num_arguments > 1:
        print(f", followed by:")
        for i in range(argv[6]):
            print(f"{i}: {sys.argv[i]}")
    else:
        print(".")