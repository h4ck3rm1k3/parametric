import variables

class Primitive:
    def __init__(self, *variables):
        self.variables = variables

#        for i, name in enumerate(self.VARIABLE_NAMES):
#            def getter(self2):
#                return self2.variables[i]
#            def setter(self2, value):
#                self2.variables[i] = value
#            prop = property(getter, setter)
#            setattr(self.__class__, name, prop)


#class Point(Primitive):
#    def __init__(self, p):
#        Primitive.__init__(self, p = p)


class LineSegment(Primitive):
#    VARIABLE_NAMES = ["p1", "p2"]

    def export_svg(self, fp, scale):
        fp.write('<line x1="{}" y1="{}" x2="{}" y2="{}" width="1" stroke="black" />\n'.format(
            int(self.variables[0].x.value * scale), int(self.variables[0].y.value * scale),
            int(self.variables[1].x.value * scale), int(self.variables[1].y.value * scale)))

#class Circle(Primitive):
#    def __init__(self, center, radius):
#        pass
#
#class ThreePointArc(Primitive):
#    def __init__(self, p1, p2, p3):
#        super().__init__(p1 = p1, p2 = p2, p3)
