import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point ({self.x}, {self.y})>"


class Building:
    def __init__(self, start, height, end):
        self.start = start
        self.height = height
        self.end = end

    def __repr__(self):
        return f"<Building with start {self.start}, end {self.end}, height {self.height}>"


class Skyline:
    def __init__(self, points):
        self.points = points

    def replicate(self, n):
        result = []
        width = self.points[-1].x
        for i in range(n):
            displacement = i * width
            result.extend([Point(p.x + displacement, p.y) for p in self.points])
        return result

    def shift_right(self, n):
        return [Point(p.x + displacement, p.y) for p in self.points]

    def shift_left(self, n):
        return self.shift_right(-n)

    def area(self):
        result = 0
        for p1, p2 in zip(self.points, self.points[1:]):
            result += (p2.x - p1.x) * p1.y
        return result

    def height(self):
        return max(p.y for p in self.points)

    def plot(self):
        xs = []
        heights = []
        widths = []
        for p1, p2 in zip(self.points, self.points[1:]):
            xs.append(p1.x)
            heights.append(p1.y)
            widths.append(p2.x-p1.x)

        plt.bar(xs, heights, widths, align="edge")
        plt.show()
        # TODO: return the plot to send to user

    def invert(self):
        x_min = self.points[0].x
        x_max = self.points[-1].x
        backward = self.points[::-1]
        new_points = [Point(x_min + x_max - p1.x, p2.y) for p1, p2 in zip(backward, backward[1:])]
        new_points.append(Point(x_max, 0))
        return new_points

    # Pre: end > start and height >= 0
    @staticmethod
    def create_from_building(self, start, height, end):
        points = [Point(start, height), Point(end, 0)]
        return Skyline(points)

    # Pre: end > start and height >= 0 for each (start, height, end) in coordinates
    @staticmethod
    def create_from_buildings(self, coordinates):
        buildings = [Building(start, height, end) for start, height, end in coordinates]
        return create_skyline(buildings)

    # Pre: xmax > xmin, h >= 0, w <= xmax-xmin 
    @staticmethod
    def create_from_random_buildings(self, n, h, w, xmin, xmax):
        buildings = []
        for _ in range(n):
            width = random.randint(1, w)
            height = random.randint(0, h)
            start = random.randint(xmin, xmax - width)
            end = start + width
            buildings.append(Building(start, height, end))
        return create_skyline(buildings)

    @staticmethod
    def add_to_result(result, x, y):
        if not result:
            result.append(Point(x, y))
        else:
            last_x = result[-1].x
            last_y = result[-1].y

            if x == last_x:
                result[-1].y = max(result[-1].y, y)
            elif y != last_y:
                result.append(Point(x, y))

    @staticmethod
    def join_two_skylines(skyline1, skyline2):
        i = 0
        j = 0
        height1 = 0
        height2 = 0
        result = []
        while i < len(skyline1) and j < len(skyline2):
            p1 = skyline1[i]
            p2 = skyline2[j]
            if p1.x < p2.x:
                height1 = p1.y
                add_to_result(result, p1.x, max(height1, height2))
                i += 1
            elif p1.x > p2.x:
                height2 = p2.y
                add_to_result(result, p2.x, max(height1, height2))
                j += 1
            else:
                height1 = p1.y
                height2 = p2.y
                add_to_result(result, p1.x, max(height1, height2))
                i += 1
                j += 1

        result.extend(skyline1[i:])
        result.extend(skyline2[j:])
        return result

    @staticmethod
    def recursive_join_skylines(buildings, left, right):
        if left == right:
            building = buildings[left]
            return [Point(buiding.start, building.height), Point(building.end, 0)]

        mid = (left + right) // 2
        buildings1 = recursive_join_skylines(buildings, left, mid)
        buildings2 = recursive_join_skylines(buildings, mid + 1, right)
        return join_two_skylines(buildings1, buildings2)

    @staticmethod
    def create_skyline(buildings):
        points = recursive_join_skylines(buildings, 0, len(buildings) - 1)
        return Skyline(points)

    @staticmethod
    def intersect_two_skylines(skyline1, skyline2):
        # TODO
        pass
