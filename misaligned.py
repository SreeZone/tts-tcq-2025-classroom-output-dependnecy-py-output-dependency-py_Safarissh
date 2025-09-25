
def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append((i * 5 + j, major, minor))
    return color_map

def format_color_entry(pair_number, major_color, minor_color):
    return f'{pair_number} | {major_color} | {minor_color}'

def print_color_map():
    color_map = get_color_map()
    for pair_number, major, minor in color_map:
        print(format_color_entry(pair_number, major, minor))
    return len(color_map)
