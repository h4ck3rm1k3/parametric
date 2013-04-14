import expressions as e
import nose.tools

def test1():
    x = e.Variable(10)
    y = e.Variable(2)

    expr = x - y

    nose.tools.assert_equals(expr.get_value(), 8)

    pds = e.numeric_diffs(expr)
    nose.tools.assert_equals(set(pds.keys()), {x, y})
    nose.tools.assert_equals(pds[x], 1)
    nose.tools.assert_equals(pds[y], -1)


def check_pds(expr, variables):
    epsilon = 0.0001
    print()

    for var in variables:
        for var2, val in variables.items():
            print(str(var2) + " = " + str(val))
            var2.set_value(val)


        pd = e.diff(expr, var)
        pd_value = pd.get_value()

        var.update_value(-epsilon)
        value1 = expr.get_value()
        var.update_value(2 * epsilon)
        value2 = expr.get_value()

        numeric_pd = (value2 - value1) / (2 * epsilon)
        print("(d {}) / (d {}) = ({} - {}) / (2 * {}) = {} (expected {} = {})".format(
            str(expr), str(var),
            value2, value1, epsilon, numeric_pd, pd, pd_value))

        nose.tools.assert_almost_equals(numeric_pd, pd_value, delta=epsilon)

def pds_test():
    x = e.Variable(5, "x")
    y = e.Variable(5, "y")
    z = e.Variable(5, "z")

    check_pds(x, {x: 10})
    check_pds(x + y + z, {x: 0.6, y: 10, z: 3})
    check_pds(x - y, {x: 0.6, y: 10})
    check_pds(x * y * z, {x: 0.6, y: 10, z: 3})
    check_pds(x / y, {x: 0.6, y: 10})
    check_pds(e.sq(x), {x: 0.6})
    check_pds(-x, {x: 0.6})
    check_pds(e.sqrt(x), {x: 0.6})
    check_pds(e.pow(x, 2), {x: 0.6})
    check_pds(e.pow(x, 5), {x: 0.6})
    check_pds(e.acos(x), {x: 0.6})

