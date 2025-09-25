# test file for tshirts
from tshirts import size

def test_sizes():
    assert(size(37) == 'S')
    assert(size(38) == 'S')  # hmm this might be wrong
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    print("tests done")

if __name__ == '__main__':
    test_sizes()
    print("All is well (maybe!)")
