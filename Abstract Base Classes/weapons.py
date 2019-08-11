class SwordMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'swipe') and callable(subclass.swipe)
                and hasattr(subclass, 'sharpen') and callable(subclass.sharpen))


# Sword will play the role of the virtual base class
class Sword(metaclass=SwordMeta):
    pass


class BroadSword:

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shink!")


class SamuraiSword:

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shink!")


class Rifle:

    def fire(self):
        print("Bang!")