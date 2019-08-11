from abc import ABCMeta, abstractmethod


# Sword will play the role of the virtual base class
class Sword(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, sub):
        return ((hasattr(sub, 'swipe') and callable(sub.swipe)
                 and
                 hasattr(sub, 'sharpen') and callable(sub.sharpen)
                 and
                 hasattr(sub, 'parry') and callable(sub.parry)
                 and
                 hasattr(sub, 'thrust') and callable(sub.thrust))
                or NotImplemented)

    @abstractmethod
    def swipe(self):
        raise NotImplementedError

    def thrust(self):
        print("Thrusting...")

    @abstractmethod
    def parry(self):
        # NotImplementedError - exception,
        # raisable in place of missing details
        raise NotImplementedError


class BroadSword(Sword):

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shink!")

    def thrust(self):
        super().thrust()

    def parry(self):
        print("Parry!")


@Sword.register
class LightSaber:

    def swipe(self):
        print("Brrrrrrrr......")


class SamuraiSword:

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shink!")


class Rifle:

    def fire(self):
        print("Bang!")
