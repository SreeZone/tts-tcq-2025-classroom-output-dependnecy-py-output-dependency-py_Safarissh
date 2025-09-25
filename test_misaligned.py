# testing the misaligned stuff
from misaligned import get_color_map, format_color_entry, print_color_map

def test_basic():
    result = print_color_map()
    assert(result == 25)

def test_formatting():
    color_map = get_color_map()
    
    entry_0 = format_color_entry(0, "White", "Blue")
    entry_10 = format_color_entry(10, "Black", "Blue")
    
    # something looks wrong with the alignment
    assert len(entry_0) == len(entry_10), f"Not aligned: '{entry_0}' vs '{entry_10}'"
    
    # check more entries
    lines = []
    for pair_number, major, minor in color_map[:12]:
        lines.append(format_color_entry(pair_number, major, minor))
    
    line_lengths = [len(line) for line in lines]
    assert len(set(line_lengths)) == 1, f"Different lengths: {line_lengths[:5]}"

if __name__ == '__main__':
    test_basic()
    test_formatting()
    print("All tests done")
