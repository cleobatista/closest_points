def merge_list(list_a, list_b):
    ordered = []
    while list_a or list_b:
        if len(list_a) and len(list_b):
            if list_a[0] < list_b[0]:
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
