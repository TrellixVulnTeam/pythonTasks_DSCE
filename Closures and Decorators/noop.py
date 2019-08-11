# example of how naive decorators can lose important metadata
import functools


def noop(f):
    # the best way to save metadata
    @functools.wraps(f)
    def noop_wrapper():
        return f()

    # a way not to lose __name__ and __doc__ without using
    # functools.wraps()
    # noop_wrapper.__name__ = f.__name__
    # noop_wrapper.__doc__ = f.__doc__
    return noop_wrapper


@noop
def hello():
    """Print a well-known data"""
    print("Hello, world")
