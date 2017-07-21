def paint_skyline_2d_array(skyline):
    """
    Counts the minimum number of horizontal brush strokes needed to paint
    a skyline mural defined by the skyline input argument array.
    
    Each entry in the skyline array coincides with a unit of height in a
    skyline mural.  Based on the input skyline arrary this function
    creates a two dimensional array where a paint block is represented as
    a boolean True and an empty block is a boolean False.  This two
    dimensional array is then traversed and horizontal brush strokes are
    counted and the result is returned.
    """
    horizontal_strokes = 0
    for y in xrange(max(skyline)):
        stroke = False
        for painted in _get_skyline(skyline, len(skyline), max(skyline))[y]:
            if horizontal_strokes > 1000000000:
                return -1
            if not stroke and painted:
                horizontal_strokes += 1
                stroke = True
            if not painted:
                stroke = False
    
    return horizontal_strokes

def _get_skyline(heights, width, height):
    """
    Builds the two dimensional array based on the heights array,
    the width of the array, and the height which is "tallest" entry in
    the array.
    """
    skyline = [[False for x in xrange(width)] for y in xrange(height)]
    for x in range(width):
        for y in range(heights[x]):
            skyline[y][x] = True
    return skyline

def paint_skyline_better_solution(skyline):
    """
    Provides a better solution to counting the minimum number of
    horizontal brush strokes needed to paint a skyline mural defined
    by the skyline input argument array.
    
    The elements in the skyline array are traversed in sequence,
    horizontal brush strokes are calculated and each element is
    decreased by 1 thus lowering the "height" of each element.  This
    process continues until all of the elements in the array are
    zero.  At this point the horizontal brush strokes are returned.
    """
    size = len(skyline)
    strokes = 0
    finished = False
    while not finished:
        if strokes > 1000000000:
            return -1
        empty_units = 0
        brush_stroke = False
        for x in xrange(size):
            if skyline[x] > 0:
                if not brush_stroke:
                    strokes += 1
                    brush_stroke = True
                skyline[x] -= 1
            elif skyline[x] == 0:
                empty_units += 1
                brush_stroke = False
            if empty_units == size:
                finished = True
    return strokes
