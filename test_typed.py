#!/usr/bin/env python
#   Test the typed version of the shapes
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

import traceback

import typed

r1 = typed.Rect(3, 4)
typed.print_info(r1, "r1")

s1 = typed.Square(1.2)
typed.print_info(s1, "s1")

t1 = typed.Triangle(3, 4, 5)
typed.print_info(t1, "t1")

t2 = typed.Triangle(1, 2, 3)
typed.print_info(t2, "t2")

# This is meant to fail at runtime
try:
    t3 = typed.Triangle(1, 2, 4)
    typed.print_info(t3, "t3")
except:
    traceback.print_exc()
    print("-" * 10)

et1 = typed.EquiTriangle(3)
typed.print_info(et1, "et1")

e1 = typed.Ellipse(2, 1)
typed.print_info(e1, "e1")

c1 = typed.Circle(2)
typed.print_info(c1, "c1")

com1 = typed.Compound(r1, s1)
typed.print_info(com1, "com1")

com2 = typed.Compound(t1, t2, et1, e1, c1)
typed.print_info(com2, "com2")

sum1 = com1 + com2
typed.print_info(sum1, "sum1")

sum2 = com1 + t1
typed.print_info(sum2, "sum2")
