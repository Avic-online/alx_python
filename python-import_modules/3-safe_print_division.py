def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # print( a, "/", b, "=", None)
        print("Inside result:", None)
        return None
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        # print("{} / {} =".format(a, b), result)
        pass
