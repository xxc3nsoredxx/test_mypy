=========
mypy Test
=========

It took me a while to come up with some nice way to test out Python's type
hinting, but I eventually settled on the classic "shapes and subclasses" thing.

Running ``mypy .`` shouldn't find any type errors. Neither should
``mypy --strict test_typed.py typed.py`` :)


The classes
===========

The following classes exist as typed and untyped versions. Each class provides
an ``area()`` and ``__repr__()`` function to return the shape's area and string
representation, respectively.

- ``Rect``: basic rectangle with a length and a width
- ``Square``: rectangle with equal length and width
- ``Triangle``: three sides with various lengths and uses triangle inequality to
  verify the sides are valid
- ``EquiTriangle``: triangle with all three sides the same length
- ``Ellipse``: ellipse with a semi-major and -minor axis length
- ``Circle``: ellipse with equal length semi-major and -minor axes
- ``Compound``: more complex shape (which is just different shapes "added"
  together)

Additionally, there is a top-level ``print_info(shape, name)`` function which
prints the string and area of the shape given. The ``name`` field is just what
you want to call the shape to distinguish it in the output.

The typed version has a few extra bits compared to the untyped version:

- ``Shape``: protocol class to define what it means to "be a shape" -- provide
  an ``area()`` function that returns a ``Number``.
- ``Number``: type alias for "anything that's an ``int`` or a ``float``"
