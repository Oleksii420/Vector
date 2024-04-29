import math


class Vector:
    def __init__(self, components):
        if isinstance(components, Vector):
            self.components = components
        else:
            self.components = list(map(float, components))

    def __str__(self):
        return " ".join(map(str, self.components))

    def dimension(self):
        return len(self.components)

    def length(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def mean(self):
        return sum(self.components) / len(self.components)

    def max_component(self):
        return max(self.components)

    def min_component(self):
        return min(self.components)
