# using decorator to change the base functionality of the existing
# function and save their previous functionality


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def northern_city():
    return 'Trom★'