#! /usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)

    if a == 1:
        print(0, "arguments.")
    elif a == 2:
        print(a-1, "argument:")
        for i in range(1, len(sys.argv)):
            print(i, sys.argv[1], sep=": ")

    else:
        print(a - 1, " arguments:")
        for i in range(1, len(sys.argv)):
            print(i, sys.argv[i], sep=": ")
