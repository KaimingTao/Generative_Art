import random
import time

random.seed(int(time.time()))


def rand_color():
    color = (
        int(random.random() * 255),
        int(random.random() * 255),
        int(random.random() * 255),
    )
    return color
