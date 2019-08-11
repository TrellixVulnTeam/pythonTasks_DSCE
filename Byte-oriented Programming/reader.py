import struct
from pprint import pprint as pp
from binascii import hexlify


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)


class Color:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return "Color({}, {}, {})".format(self.red, self.green, self.blue)


class Vertex:

    def __init__(self, vector, color):
        self.vector = vector
        self.color = color

    def __repr__(self):
        return "Vertex({}, {})".format(self.vector, self.color)


def make_colored_vertex(x, y, z, red, green, blue):
    return Vertex(Vector(x, y, z),
                  Color(red, green, blue))


def main():
    with open('color.bin', 'rb') as f:
        buffer = f.read()

    vertices = []
    for x, y, z, red, green, blue in struct.iter_unpack('@3f3Hxx', buffer):
        vertex = make_colored_vertex(x, y, z, red, green, blue)
        vertices.append(vertex)

    pp(vertices)


if __name__ == '__main__':
    main()