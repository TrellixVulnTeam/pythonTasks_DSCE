import sys


def main(filename):
    with open(filename, mode="rt", encoding='utf-8') as f:
        for line in f:
            sys.stdout.write(line)


if __name__ == '__main__':
    main(sys.argv[1])

