def list_arg (*argv):
    argv = ["Hello", "Holberton", "School", 98, "Battery", "street"]
    start = 0
    for start in argv:
        print("this is it {}".format(argv), end="")
        start = start + 1
    return argv