#   The untyped shapes
#   Copyright (C) 2022  Oskari Pirhonen <xxc3ncoredxx@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math

# Basic rectangle defined by its length and width
class Rect:
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def __repr__ (self):
        return f"Rect with length: {self.length} width: {self.width}"

    def area (self):
        return self.length * self.width

# Equilateral rectangle
class Square (Rect):
    def __init__ (self, side):
        self.side = side

        super(Square, self).__init__(side, side)

    def __repr__ (self):
        return f"Square of side: {self.side}"

# Basic triangle defined by the lengths of its sides
class Triangle:
    def __init__ (self, A, B, C):
        # Use the triangle inequality to validate the side lengths
        ab = A + B
        ac = A + C
        bc = B + C

        if (
               ab < C
            or ac < B
            or bc < A
        ):
            raise ValueError(f"invalid side lengths: {A}, {B}, {C}")

        self.A = A
        self.B = B
        self.C = C

    def __repr__ (self):
        return f"Triangle with sides: {self.A} {self.B} {self.C}"

    # Heron's formula
    def area (self):
        a =  self.A + self.B - self.C
        b =  self.A - self.B + self.C
        c = -self.A + self.B + self.C
        d =  self.A + self.B + self.C

        return math.sqrt(a * b * c * d) / 4

# The square of the triangle world
class EquiTriangle (Triangle):
    def __init__ (self, side):
        self.side = side

        super(EquiTriangle, self).__init__(side, side, side)

    def __repr__ (self):
        return f"EquiTriangle with sides: {self.side}"

# Basic ellipse defined by the lengths of its semi-major (horizontal) and
# semi-minor (veritcal) axes
class Ellipse:
    # a: semi-major axis
    # b: semi-minor axis
    def __init__ (self, a, b):
        self.a = a
        self.b = b

    def __repr__ (self):
        return f"Ellipse with semi-major: {self.a} semi-minor: {self.b}"

    def area (self):
        return math.pi * self.a * self.b

# The elliptical version of a square
class Circle (Ellipse):
    def __init__ (self, r):
        self.r = r

        super(Circle, self).__init__(r, r)

    def __repr__ (self):
        return f"Circle with radius: {self.r}"

# A compound shape formed by adding a bunch of shapes together
class Compound:
    # Want some shapes to combine
    def __init__ (self, *args):
        self.shapes = args

    def __add__ (self, other):
        if isinstance(other, Compound):
            return Compound(*self.shapes, *other.shapes)
        else:
            return Compound(*self.shapes, other)

    def __repr__ (self):
        return str(list(self.shapes))

    def area (self):
        return sum([s.area() for s in self.shapes])

# Print some deets about the given shape
def print_info (shape, name):
    print(f"{name} = {shape}")
    print(f"area = {shape.area()}")
    print("-" * 10)
