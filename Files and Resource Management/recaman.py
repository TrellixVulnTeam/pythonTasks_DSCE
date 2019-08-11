import sys
from itertools import count, islice


def sequence():
    """Generate Recaman's sequence"""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """Write Recama's sequence to a text file"""
    with open(filename, mode='wt', encoding='utf-8') as f:
        # islice - Make an iterator that returns selected elements from the iterable. The second argument - stop value
        f.writelines("{0}\n".format(r)
                     for r in islice(sequence(), num + 1))


if __name__ == '__main__':
    write_sequence(filename=sys.argv[1],
                   num=int(sys.argv[2]))