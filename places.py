from numpy import sqrt
from random import uniform, choice
import string

import plotly.graph_objs as go

class Places:

    def __init__(self, places = None, n=None, amplitude=100):
        self.places = places
        if not places:
            assert n, "if you don't give the places, give me a number of places to generate random n places"
            letters = string.ascii_lowercase
            self.places = {''.join(choice(letters) for i in range(5)): (uniform(0,amplitude), uniform(0,amplitude)) for j in range(n)}
        else:
            assert type(places) == dict, "places must be a dict, if you refering to n, please name it"


    def merge_list(self, list_a, list_b):
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


    def merge_sort(self, _list):
        ordered = []
        if len(_list) > 1:
            mid = len(_list) // 2
            left = self.merge_sort(_list[0:mid])
            right = self.merge_sort(_list[mid:])
            ordered = self.merge_list(left, right)
            return ordered
        else:
            return _list


    def sort_dict_by_value(self, _dict):
        _list = [(x, i) for (x, y), i in zip(list(_dict.values()), list(_dict))] # O(n)
        index = [i for x, i in self.merge_sort(_list)] # O(n)
        ordered_keys = {i:_dict[i] for i in index} # O(n)
        return ordered_keys


    def distance(self, point_1, point_2):
        return sqrt(sum(((point_1[0] - point_2[0])**2, (point_1[1] - point_2[1])**2)))

    def dict_to_list(self, _dict):
        return list(zip(_dict.values(), _dict.keys()))

    #list format [[(x,y), name]]
    def closest_pair(self, _list = None): # must be a sorted list
        if not _list:
            _list = self.dict_to_list(self.places)
            _list = self.merge_sort((_list))
        if len(_list) > 2:
            middle = len(_list) // 2
            left = self.closest_pair(_list[:middle])
            right = self.closest_pair(_list[middle:])
            left = right if not left else left
            right = left if not right else right
            closest = left if min(left[0], right[0]) == left[0] else right
            return self.min_from_middle(middle, _list, closest)
        elif len(_list) == 2:
            return self.distance(_list[0][0], _list[1][0]), _list[0][1], _list[1][1]
        else:
            return

    def min_from_middle(self, middle, _list, closest):
        middle_x = (_list[middle][0][0] + _list[middle - 1][0][0]) / 2
        upper = middle_x + closest[0]
        lower = middle_x - closest[0]
        points = [item for item in _list if (lower <= item[0][0] <= upper)]
        for i, point in enumerate(points):
            for j, neighbor in enumerate(points[min(i + 1, len(points)): min(len(points),i+8)]):
                dist = self.distance(point[0], neighbor[0])
                if dist < closest[0]:
                    closest = dist, point[1], neighbor[1]

        return closest

    def plot(self, show_closest=False):
        x, y = zip(*self.places.values())
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode='markers'
            )
        )

        if show_closest:
            closest = self.closest_pair()[1:]
            x0 = self.places[closest[0]][0]
            y0 = self.places[closest[0]][1]
            x1 = self.places[closest[1]][0]
            y1 = self.places[closest[1]][1]
            fig.add_trace(
                go.Scatter(
                    x=[x0, x1],
                    y=[y0, y1],
                    mode='markers',
                    marker=dict(
                        size=16,
                        color="red",
                    )
                )
            )
        fig.show()

if __name__ == '__main__':
    letters = string.ascii_lowercase
    places = Places(n=20)
    breakpoint()

    # places_list = dict_to_list(places)
    # places_list = merge_sort(places_list)
    # print(closest_pair(places_list))

