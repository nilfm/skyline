import skyline
from skyline import Building, Skyline
import matplotlib.pyplot as plt

sky = Skyline.create_from_building(1, 2, 3)

sky2 = Skyline.create_from_building(3, 4, 6)

sky = Skyline.join_two_skylines(sky, sky2)

sky = sky.replicate(3)
sky = sky.invert()

sky3 = Skyline.create_from_building(1, 3, 10)
Skyline.intersect_two_skylines(sky, sky3)
