import skyline
from skyline import Building, Skyline
import matplotlib.pyplot as plt

buildings = [
    Building(-1, 10, 3),
    Building(0, 3, 2),
    Building(1, 1, 6),
    Building(3, 5, 9),
    Building(4, 2, 8),
    Building(15, 2, 21),
    Building(16, 4, 19),
    Building(17, 6, 18),
]

buildings2 = [
    Building(0, 4, 1),
    Building(1, 2, 6),
    Building(3, 5, 9),
    Building(4, 2, 8),
    Building(15, 2, 21),
    Building(16, 3, 19),
    Building(17, 10, 18),
]

sky = Skyline.create_skyline(buildings)
sky2 = Skyline.create_skyline(buildings2)
inter = Skyline.intersect_two_skylines(sky, sky2)
plt.figure(2)
a = inter.plot()
