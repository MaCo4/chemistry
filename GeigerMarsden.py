from random import random
from math import sqrt, ceil, pi


"""
These values are taken from the MIT experiment, where the gold nucleus are the styrofoam balls in the grid,
and the alpha particles are the ping-pong balls thrown. 
"""
gold_nucleus_radius = 0.0125  # in meters
alpha_particle_radius = 0.02  # in meters


class Particle:
    x = 0
    y = 0
    radius = 0

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


def check_overlap(p1: Particle, p2: Particle):
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) < (p1.radius + p2.radius)


def build_nuclei_grid(num_nuclei, width, height):
    nuclei = []
    num_nuclei_x = num_nuclei_y = int(ceil(sqrt(num_nuclei)))
    dist_x = width / num_nuclei_x
    dist_y = height / num_nuclei_y
    offset_x = dist_x / 2
    offset_y = dist_y / 2

    for x in range(num_nuclei_x):
        for y in range(num_nuclei_y):
            if len(nuclei) < num_nuclei:
                nuclei.append(Particle(dist_x * x + offset_x, dist_y * y + offset_y, gold_nucleus_radius))
    return nuclei


def geiger_marsden(gold_foil_area, num_atoms, num_alpha_emitted):
    gold_foil_width = gold_foil_height = sqrt(gold_foil_area)
    nuclei = build_nuclei_grid(num_atoms, gold_foil_width, gold_foil_height)

    num_alpha_deflected = 0
    for i in range(num_alpha_emitted):
        emitted_particle = Particle(random() * gold_foil_width, random() * gold_foil_height, alpha_particle_radius)
        for nucleus in nuclei:
            if check_overlap(emitted_particle, nucleus):
                # Assumes the alpha particle is deflected if it "overlaps" with a gold nucleus
                num_alpha_deflected += 1

    print("Num alpha particles emitted: {}, num alpha particles deflected: {}".format(num_alpha_emitted, num_alpha_deflected))

    nucleus_radius = sqrt((num_alpha_deflected / num_alpha_emitted) * (gold_foil_area / (num_atoms * pi)))
    return nucleus_radius


if __name__ == "__main__":
    """
    Runs an experiment with the same values as in the MIT experiment. It estimates the radius of the
    styrofoam balls in the grid (the "gold nuclei"). All values are in meters.
    
    The principle is the same as for estimating the gold nuclei radius by emitting
    alpha particles, but with other parameters.
    """

    radius = geiger_marsden(gold_foil_area=1.39, num_atoms=119, num_alpha_emitted=266)
    print("Nuclei radius: {}".format(radius))
