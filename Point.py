class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x;
        self.y = y;

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y);
        #return self;

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y);

    def __mul__(self, other):
        return self.x * other.x + self.y + other.y;

    def __rmul__(self, other):
        return Point(self.x * other, self.y * other);

    def front_and_back(front):
        import copy;
        back = copy.copy(front);
        back.reverse();
        print(str(front) + str(back));

    def reverse(self):
        self.x, self.y = self.y, self.x;
