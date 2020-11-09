def printhelloworld(msg):
    """
    docstring
    """
    if type(msg) != str:
        print('type is wrong!')
    else:
        print(msg+'helloworld!')
    return msg


def main():
    printhelloworld(1)


if __name__ == "__main__":
    main()
