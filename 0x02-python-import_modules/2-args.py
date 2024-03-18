#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argnums = len(sys.argv) - 1
    if argnums == 0:
        print("0 arguments.")
    elif argnums == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argnums))
    for i in range (argnums):
            argv = (sys.argv[i + 1])
            print("{}; {}".format(i + 1, argv))
