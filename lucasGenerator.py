def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


def main():
    # example for showing infinity sequence
    for x in lucas():
        print(x, " ")


if __name__ == '__main__':
    main()