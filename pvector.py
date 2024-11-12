# Eigene PVector-Klasse um die PVector-Klasse von p5 zu ersetzen

class PVector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def __repr__(self):
        return f'PVector({self.x}, {self.y}, {self.z})'