class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Point):
            other = other.value
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return (self.x, self.y)

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
        return False




