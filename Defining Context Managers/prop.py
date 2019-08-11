import contextlib


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally')
    except Exception:
        print(name, 'received an exception!')
        if propagate:
            raise


def main():
    with propagater('outer', True), propagater('inner', False):
        raise TypeError('Cannot convert lead into gold')
    with propagater('outer', False), propagater('inner', True):
        raise TypeError('Cannot convert lead into gold')


if __name__ == '__main__':
    main()