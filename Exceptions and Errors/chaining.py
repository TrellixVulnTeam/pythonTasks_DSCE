import math
import traceback


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope can not be vertical.") from e


def main():
    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e.__traceback__)
        traceback.print_tb(e.__traceback__)


if __name__ == '__main__':
    main()
    print('Finished.')