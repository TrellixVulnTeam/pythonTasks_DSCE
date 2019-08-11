class LoggingProxy:

    def __init__(self, target):
        super().__setattr__('target', target)

    def __getattribute__(self, name):
        target = super().__getattribute__('target')

        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        print("Retrieved attribute {!r} = {!r} from {!r}".format(name, value, target))
        return

    def __setattr__(self, name, value):
        target = super().__getattribute__('target')

        try:
            setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        print("Set attribute {!r} = {!r} from {!r}".format(name, value, target))
        return value

    def __repr__(self):
        target = super().__getattribute__('target')
        repr_callable = getattr(target, '__repr__')
        return repr_callable()
