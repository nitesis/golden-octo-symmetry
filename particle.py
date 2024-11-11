# Particle class for simulating particles in a particle system

import random
from p5 import PVector

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.uniform(5, 10)
        self.color = (255, 215, 0)  # Goldgelb
        self.velocity = PVector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = PVector(0, 0)

    def update(self):
        self.velocity.add(self.acceleration)
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.acceleration.mult(0)

    def display(self):
        fill(self.color[0], self.color[1], self.color[2])
        ellipse(self.x, self.y, self.size, self.size)

    def apply_force(self, force):
        self.acceleration.add(force)

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def create_particle(self, x, y):
        p = Particle(x, y)
        self.particles.append(p)

    def update(self):
        for p in self.particles:
            p.update()
            p.display()

    def clear_particles(self):
        self.particles.clear()
