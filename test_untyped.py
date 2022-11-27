#!/usr/bin/env python

import traceback

import untyped

r1 = untyped.Rect(3, 4)
untyped.print_info(r1, "r1")

s1 = untyped.Square(1.2)
untyped.print_info(s1, "s1")

t1 = untyped.Triangle(3, 4, 5)
untyped.print_info(t1, "t1")

t2 = untyped.Triangle(1, 2, 3)
untyped.print_info(t2, "t2")

# This is meant to fail at runtime
try:
    t3 = untyped.Triangle(1, 2, 4)
    untyped.print_info(t3, "t3")
except:
    traceback.print_exc()
    print("-" * 10)

et1 = untyped.EquiTriangle(3)
untyped.print_info(et1, "et1")

e1 = untyped.Ellipse(2, 1)
untyped.print_info(e1, "e1")

c1 = untyped.Circle(2)
untyped.print_info(c1, "c1")

com1 = untyped.Compound(r1, s1)
untyped.print_info(com1, "com1")

com2 = untyped.Compound(t1, t2, et1, e1, c1)
untyped.print_info(com2, "com2")

sum1 = com1 + com2
untyped.print_info(sum1, "sum1")

sum2 = com1 + t1
untyped.print_info(sum2, "sum2")
