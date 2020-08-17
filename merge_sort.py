from numpy import sqrt
def merge_list(list_a, list_b):
    ordered = []
    while list_a or list_b:
        if len(list_a) and len(list_b):
            if list_a[0][0] < list_b[0][0]:
                ordered.append(list_a.pop(0))
            else:
                ordered.append(list_b.pop(0))
        elif len(list_a):
            ordered.extend(list_a)
            list_a = []
        elif len(list_b):
            ordered.extend(list_b)
            list_b = []
    return ordered


def merge_sort(_list):
    ordered = []
    if len(_list) > 1:
        mid = len(_list) // 2
        left = merge_sort(_list[0:mid])
        right = merge_sort(_list[mid:])
        ordered = merge_list(left, right)
        return ordered
    else:
        return _list


def sort_dict_by_value(_dict):
    _list = [(x, i) for (x, y), i in zip(list(_dict.values()), list(_dict))] # O(n)
    index = [i for x, i in merge_sort(_list)] # O(n)
    ordered_keys = {i:_dict[i] for i in index} # O(n)
    return ordered_keys


def distance(point_1, point_2):
   return sqrt(sum(((point_1[0] - point_2[0])**2, (point_1[1] - point_2[1])**2)))

def dict_to_list(_dict):
    return list(zip(_dict.values(), _dict.keys()))

#list format [[(x,y), name]]

def closest_pair(_list): # must be a sorted list
    if len(_list) > 2:
        middle = len(_list) // 2
        left = closest_pair(_list[:middle])
        right = closest_pair(_list[middle:])
        closest = left if min(left[0], right[0]) == left[0] else right
        return min_from_middle(middle, _list, closest)
    else:
        return distance(_list[0][0], _list[1][0]), _list[0][1], _list[1][1]


def min_from_middle(middle, _list, closest):
    middle_x = (_list[middle][0][0] - _list[middle + 1][0][0]) / 2
    upper = middle_x + closest[0]
    lower = middle_x - closest[0]
    points = [item for item in _list if (lower <= item[0][0] <= upper)]
    for i, point in enumerate(points):
        for j, neighbor in enumerate(points[min(i + 1, len(points)): min(len(points),i+8)]):
            dist = distance(point, neighbor)
            if dist < delta:
                closest = dist, point[1], neighbor[1]

    return closest

