import random
import matplotlib.pyplot as plt
from io import BytesIO

class Point:
    def __init__(self, x, y):
        """
        Constructs a Point object from its x and y coordinates
        Input: x and y coordinates
        Complexity: Constant
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Returns a string representing a Point object
        """
        return f"<Point ({self.x}, {self.y})>"


class Building:
    def __init__(self, start, height, end):
        """
        Constructs a Building object from its start and end x-coordinates and height
        Input: Start and end x-coordinates and height
        Complexity: Constant
        """
        self.start = Point(start, height)
        self.end = Point(end, 0)

    def __repr__(self):
        """
        Returns a string representing a Building object
        """
        return f"<Building with start {self.start} and end {self.end}>"


class Skyline:
    def __init__(self, points):
        """
        Constructs a Skyline object from the points that form it
        Input: Array of Point objects
        Complexity: Constant
        """
        self.points = points

    def __repr__(self):
        result = ""
        for point in self.points:
            result += str(point) + "\n"
        return result

    @staticmethod
    def add(a, b):
        if isinstance(b, int):
            return a.shift_right(b)
        else:
            return Skyline.join_two_skylines(a, b)
            
    @staticmethod
    def prod(a, b):
        if isinstance(b, int):
            return a.replicate(b)
        else:
            return Skyline.intersect_two_skylines(a, b)
    
    @staticmethod
    def subtract(a, b):
        return a.shift_left(b)

    def replicate(self, n):
        """
        Constructs a Skyline object with the result of replicating the instance n times
        Input: Number of times to be replicated
        Complexity: Linear in the number of points of the result
        """
        result = []
        width = self.points[-1].x - self.points[0].x
        for i in range(n):
            displacement = i * width
            result.extend([Point(p.x + displacement, p.y) for p in self.points[:-1]])
        last_x = self.points[-1].x + (n-1)*width
        result.append(Point(last_x, 0))
        
        return Skyline(result)

    def shift_right(self, n):
        """
        Constructs a Skyline object with the result of shifting the instance right n units
        Input: Number of units to be shifted
        Complexity: Linear in the number of points
        """
        return Skyline([Point(p.x + displacement, p.y) for p in self.points])

    def shift_left(self, n):
        """
        Constructs a Skyline object with the result of shifting the instance left n units
        Input: Number of units to be shifted
        Complexity: Linear in the number of points
        """
        return self.shift_right(-n)

    def invert(self):
        """
        Constructs a Skyline object with the result of reflecting the skyline
        Complexity: Linear in the number of points
        """
        x_min = self.points[0].x
        x_max = self.points[-1].x
        backward = self.points[::-1]
        new_points = [Point(x_min + x_max - p1.x, p2.y) for p1, p2 in zip(backward, backward[1:])]
        new_points.append(Point(x_max, 0))
        return Skyline(new_points)

    def area(self):
        """
        Returns the area under the skyline
        Complexity: Linear in the number of points
        """
        result = 0
        for p1, p2 in zip(self.points, self.points[1:]):
            result += (p2.x - p1.x) * p1.y
        return result

    def height(self):
        """
        Returns the maximum height that the skyline achieves
        Complexity: Linear in the number of points
        """
        return max(p.y for p in self.points)

    def plot(self):
        """
        Returns a BytesIO buffer that contains the plot of the skyline
        Complexity: Linear in the number of points
        """
        xs = []
        heights = []
        widths = []
        for p1, p2 in zip(self.points, self.points[1:]):
            xs.append(p1.x)
            heights.append(p1.y)
            widths.append(p2.x - p1.x)
        
        plt.figure()
        plt.bar(xs, heights, widths, align="edge")
        buf = BytesIO()
        plt.savefig(buf)
        buf.seek(0)
        return buf

    # Necessary: end > start and height >= 0
    @staticmethod
    def create_from_building(start, height, end):
        """
        Constructs a Skyline object with a single building
        Input: Start and end x-coordinates and height
        Complexity: Constant
        """
        if end <= start or height < 0:
            raise Exception()
            
        building = Building(start, height, end)
        points = [building.start, building.end]
        return Skyline(points)

    @staticmethod
    def create_from_buildings(skylines):
        """
        Constructs a Skyline object from a list of skylines
        Input: A list of Skyline objects
        Complexity: N*log(N) where N is the number of skylines
        """
        return Skyline.create_skyline(skylines)

    # Necessary: xmax > xmin, h >= 0, w <= xmax-xmin
    @staticmethod
    def create_from_random_buildings(n, h, w, xmin, xmax):
        """
        Constructs a Skyline object from parameters for random building generation
        Input: Number of buildings n, maximum height h, maximum width w, minimum x-coordinate xmin, maximum x-coordinate xmax
        Complexity: n*log(n)
        """
        if xmax <= xmin or h < 0 or w > xmax-xmin:
            raise Exception()
            
        skylines = []
        for _ in range(n):
            width = random.randint(1, w)
            height = random.randint(0, h)
            start = random.randint(xmin, xmax - width)
            end = start + width
            building = Building(start, height, end)
            points = [building.start, building.end]
            skylines.append(Skyline(points))
        return Skyline.create_skyline(skylines)

    @staticmethod
    def add_to_result(result, x, y, comparator=max):
        """
        Helper method to add a Point to the result array, taking into account edge cases where the last point in result has the same x or y coordinate as the point given
        Input: Result array, (x, y) coordinates of the new Point, comparator function which will be max for union and min for intersection
        Complexity: Constant
        """
        if not result:
            result.append(Point(x, y))
        else:
            last_x = result[-1].x
            last_y = result[-1].y

            if x == last_x:
                result[-1].y = comparator(result[-1].y, y)
            elif y != last_y:
                result.append(Point(x, y))

    @staticmethod
    def join_two_skylines(skyline1, skyline2):
        """
        Joins two Skyline objects into another Skyline object which is their union
        Input: Two Skyline objects
        Complexity: Linear in the number of points of both skylines
        """
        i = 0
        j = 0
        height1 = 0
        height2 = 0
        result = []
        while i < len(skyline1.points) and j < len(skyline2.points):
            p1 = skyline1.points[i]
            p2 = skyline2.points[j]
            if p1.x < p2.x:
                height1 = p1.y
                Skyline.add_to_result(result, p1.x, max(height1, height2))
                i += 1
            elif p1.x > p2.x:
                height2 = p2.y
                Skyline.add_to_result(result, p2.x, max(height1, height2))
                j += 1
            else:
                height1 = p1.y
                height2 = p2.y
                Skyline.add_to_result(result, p1.x, max(height1, height2))
                i += 1
                j += 1

        result.extend(skyline1.points[i:])
        result.extend(skyline2.points[j:])
        return Skyline(result)

    @staticmethod
    def recursive_join_skylines(skylines, left, right):
        """
        Creates a Skyline from a list of buildings using a method similar to merge-sort
        Input: List of Building objects, indices (left, right) that delimit the buildings to treat
        Complexity: O(N*logN) where N is the number of buildings
        """
        if left == right:
            return skylines[left]

        mid = (left + right) // 2
        skylines1 = Skyline.recursive_join_skylines(skylines, left, mid)
        skylines2 = Skyline.recursive_join_skylines(skylines, mid + 1, right)
        return Skyline.join_two_skylines(skylines1, skylines2)

    @staticmethod
    def create_skyline(skylines):
        """
        Creates a Skyline from a list of skylines using a method similar to merge-sort
        Input: List of Skyline objects
        Complexity: O(N*logN) where N is the number of skylines        
        """
        return Skyline.recursive_join_skylines(skylines, 0, len(skylines) - 1)

    @staticmethod
    def intersect_two_skylines(skyline1, skyline2):
        """
        Creates a Skyline object that is the intersection of two Skylines
        Input: Two Skyline objects
        Complexity: Linear in the number of points in both skylines
        """
        result = []
        i = 0
        j = 0
        while i < len(skyline1.points)-1 and j < len(skyline2.points)-1:
            p1 = skyline1.points[i]
            p2 = skyline2.points[j]
            q1 = skyline1.points[i+1]
            q2 = skyline2.points[j+1]

            # 6 possible relative positions
            if p2.x > q1.x:
                i += 1
            
            elif p1.x > q2.x:
                j += 1
                
            elif p1.x <= p2.x and q1.x >= q2.x:
                Skyline.add_to_result(result, p2.x, min(p1.y, p2.y), min)
                j += 1
            
            elif p2.x <= p1.x and q2.x >= q1.x:
                Skyline.add_to_result(result, p1.x, min(p1.y, p2.y), min)
                i += 1
                
            elif p1.x <= p2.x and q1.x <= q2.x:
                Skyline.add_to_result(result, p2.x, min(p1.y, p2.y), min)
                i += 1 
                
            else:
                Skyline.add_to_result(result, p1.x, min(p1.y, p2.y), min)
                j += 1
                            
        last1 = skyline1.points[-1]
        last2 = skyline2.points[-1]
        Skyline.add_to_result(result, min(last1.x, last2.x), 0, min)
        
        return Skyline(result)
