"""Benchmarks for Charshape."""

from polyshell import reduce_polygon


def polyshell_charshape(poly, eps):
    return reduce_polygon(poly, "epsilon", eps, method="charshape")


RUNNERS = [polyshell_charshape]
LABELS = ["polyshell (charshape)"]

BENCHMARKS = list(zip(RUNNERS, LABELS))
