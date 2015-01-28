import random
import time


def generate_random():
    seed = time.time()
    print "seed: %s" % seed
    random.seed(time.time())

    print random.uniform(0, 5)

    print random.randint(0, 5)


generate_random()