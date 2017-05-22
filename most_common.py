def most_common(data):
    """
    Returns the top most often encountered in the data list
    """
    tracker = {}
    top = [data[0]]
    count = 0
    for element in data:
        if tracker.get(element):
            tracker[element] += 1
        else:
            tracker[element] = 1
        if tracker[element] > count:
            count = tracker[element]
            top = [element]
        elif tracker[element] == count:
            top.append(element)
    return top

def most_common_x(data, top_count=3):
    """
    Returns the top most often encountered elements in the data list.
    TODO - Can probably be made more efficient if top elements are
    managed in the initial for loop.
    """
    tracker = {}
    for element in data:
        if tracker.get(element):
            tracker[element] += 1
        else:
            tracker[element] = 1
    
    top_x = []
    for k, v in tracker.items():
        if len(top_x) < top_count:
            top_x.append((k, v))
        elif top_x[0][1] < v:
            top_x.pop(0)
            top_x.append((k, v))
        top_x = sorted(top_x, key=lambda x: x[1])
    return [x[0] for x in top_x]
