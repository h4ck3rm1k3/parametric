class ExpandableVariable:
    def expand(self):
        """Expand compound variables. Returns set of Variable instances."""
        raise NotImplementedError()

class Variable(ExpandableVariable):
    """ Variable used as an parameter of the model.
    Keeps a set of drawables that use it. """

    def __init__(self, value):
        self.value = value

    def expand(self):
        """Expand compound variables. Returns set of single variable instances."""
        return {self}

class ControlPoint2D(ExpandableVariable):
    """ A pair of variables.
    Control point is never a part of output shape. """
    def __init__(self, x, y):
        self.x = Variable(x)
        self.y = Variable(y)

    def expand(self):
        """Expand compound variables. Returns set of single variable instances."""
        return {self.x, self.y}
