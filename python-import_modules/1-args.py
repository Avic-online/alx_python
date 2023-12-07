# argument_printer.py

# if __name__ == "__main__":
#     import sys

#     # Get the number of arguments
#     num_arguments = len(sys.argv) - 1

#     # Print the number of arguments and their list
#     print(f"Number of argument(s): {num_arguments}", end="")
    
#     if num_arguments == 1:
#         print(f", followed by:\n1: {sys.argv[1]}")
#     elif num_arguments > 1:
#         print(f", followed by:")

#         # Print each argument with its position
#         for i in range(1, num_arguments + 1):
#             print(f"{i}: {sys.argv[i]}")
#     else:
#         print(".")