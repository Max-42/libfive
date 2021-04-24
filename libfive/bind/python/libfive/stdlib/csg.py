"""
Python bindings to the libfive CAD kernel

DO NOT EDIT BY HAND!
This file is automatically generated from libfive/stdlib/stdlib.h

It was last generated on 2021-04-08 20:30:18 by user mkeeter

This is libfive.stdlib.csg
"""

from libfive.ffi import libfive_tree, tfloat, tvec2, tvec3, stdlib
from libfive.shape import Shape

import ctypes

stdlib._union.argtypes = [libfive_tree, libfive_tree]
stdlib._union.restype = libfive_tree
def union(a, b):
    """ Returns the union of two shapes
    """
    args = [Shape.wrap(a), Shape.wrap(b)]
    return Shape(stdlib._union(
        args[0].ptr,
        args[1].ptr))

stdlib.intersection.argtypes = [libfive_tree, libfive_tree]
stdlib.intersection.restype = libfive_tree
def intersection(a, b):
    """ Returns the intersection of two shapes
    """
    args = [Shape.wrap(a), Shape.wrap(b)]
    return Shape(stdlib.intersection(
        args[0].ptr,
        args[1].ptr))

stdlib.inverse.argtypes = [libfive_tree]
stdlib.inverse.restype = libfive_tree
def inverse(a):
    """ Returns a shape that's the inverse of the input shape
    """
    args = [Shape.wrap(a)]
    return Shape(stdlib.inverse(
        args[0].ptr))

stdlib.difference.argtypes = [libfive_tree, libfive_tree]
stdlib.difference.restype = libfive_tree
def difference(a, b):
    """ Subtracts the second shape from the first
    """
    args = [Shape.wrap(a), Shape.wrap(b)]
    return Shape(stdlib.difference(
        args[0].ptr,
        args[1].ptr))

stdlib.offset.argtypes = [libfive_tree, tfloat]
stdlib.offset.restype = libfive_tree
def offset(a, o):
    """ Expand or contract a given shape by an offset
        Positive offsets expand the shape; negative offsets shrink it
    """
    args = [Shape.wrap(a), Shape.wrap(o)]
    return Shape(stdlib.offset(
        args[0].ptr,
        args[1].ptr))

stdlib.clearance.argtypes = [libfive_tree, libfive_tree, tfloat]
stdlib.clearance.restype = libfive_tree
def clearance(a, b, offset):
    """ Expands shape b by the given offset then subtracts it from shape a
    """
    args = [Shape.wrap(a), Shape.wrap(b), Shape.wrap(offset)]
    return Shape(stdlib.clearance(
        args[0].ptr,
        args[1].ptr,
        args[2].ptr))

stdlib.shell.argtypes = [libfive_tree, tfloat]
stdlib.shell.restype = libfive_tree
def shell(a, offset):
    """ Returns a shell of a shape with the given offset
    """
    args = [Shape.wrap(a), Shape.wrap(offset)]
    return Shape(stdlib.shell(
        args[0].ptr,
        args[1].ptr))

stdlib.blend_expt.argtypes = [libfive_tree, libfive_tree, tfloat]
stdlib.blend_expt.restype = libfive_tree
def blend_expt(a, b, m):
    """ Blends two shapes by the given amount using exponents
    """
    args = [Shape.wrap(a), Shape.wrap(b), Shape.wrap(m)]
    return Shape(stdlib.blend_expt(
        args[0].ptr,
        args[1].ptr,
        args[2].ptr))

stdlib.blend_expt_unit.argtypes = [libfive_tree, libfive_tree, tfloat]
stdlib.blend_expt_unit.restype = libfive_tree
def blend_expt_unit(a, b, m):
    """ Blends two shapes by the given amount using exponents,
        with the blend term adjusted to produce results approximately
        resembling blend_rough for values between 0 and 1.
    """
    args = [Shape.wrap(a), Shape.wrap(b), Shape.wrap(m)]
    return Shape(stdlib.blend_expt_unit(
        args[0].ptr,
        args[1].ptr,
        args[2].ptr))

stdlib.blend_rough.argtypes = [libfive_tree, libfive_tree, tfloat]
stdlib.blend_rough.restype = libfive_tree
def blend_rough(a, b, m):
    """ Blends two shapes by the given amount, using a fast-but-rough
        CSG approximation that may not preserve gradients
    """
    args = [Shape.wrap(a), Shape.wrap(b), Shape.wrap(m)]
    return Shape(stdlib.blend_rough(
        args[0].ptr,
        args[1].ptr,
        args[2].ptr))

stdlib.blend_difference.argtypes = [libfive_tree, libfive_tree, tfloat, tfloat]
stdlib.blend_difference.restype = libfive_tree
def blend_difference(a, b, m, o=0):
    """ Blends the subtraction of b, with optional offset o,
        from a, with smoothness m
    """
    args = [Shape.wrap(a), Shape.wrap(b), Shape.wrap(m), Shape.wrap(o)]
    return Shape(stdlib.blend_difference(
        args[0].ptr,
        args[1].ptr,
        args[2].ptr,
        args[3].ptr))

stdlib.morph.argtypes = [libfive_tree, libfive_tree, tfloat]
stdlib.morph.restype = libfive_tree
def morph(a, b, m):
    """ Morphs between two shapes.
        m = 0 produces a, m = 1 produces b
    """
    args = [Shape.wrap(a), Shape.wrap(b), Shape.wrap(m)]
    return Shape(stdlib.morph(
        args[0].ptr,
        args[1].ptr,
        args[2].ptr))

stdlib.loft.argtypes = [libfive_tree, libfive_tree, tfloat, tfloat]
stdlib.loft.restype = libfive_tree
def loft(a, b, zmin, zmax):
    """ Produces a blended loft between a (at zmin) and b (at zmax)
        a and b should be 2D shapes (i.e. invariant along the z axis)
    """
    args = [Shape.wrap(a), Shape.wrap(b), Shape.wrap(zmin), Shape.wrap(zmax)]
    return Shape(stdlib.loft(
        args[0].ptr,
        args[1].ptr,
        args[2].ptr,
        args[3].ptr))

stdlib.loft_between.argtypes = [libfive_tree, libfive_tree, tvec3, tvec3]
stdlib.loft_between.restype = libfive_tree
def loft_between(a, b, lower, upper):
    """ Produces a blended loft between a (at lower.z) and b (at upper.z),
        with XY coordinates remapped to slide between lower.xy and upper.xy.
        a and b should be 2D shapes (i.e. invariant along the z axis)
    """
    args = [Shape.wrap(a), Shape.wrap(b), list([Shape.wrap(i) for i in lower]), list([Shape.wrap(i) for i in upper])]
    return Shape(stdlib.loft_between(
        args[0].ptr,
        args[1].ptr,
        tvec3(*[a.ptr for a in args[2]]),
        tvec3(*[a.ptr for a in args[3]])))

blend = blend_expt_unit
################################################################################
# Hand-written functions which allow for arbitrary numbers of arguments
import functools

_prev_union = union
def union(a, *args):
    return functools.reduce(_prev_union, args, a)
union.__doc__ = _prev_union.__doc__

_prev_intersection = intersection
def intersection(a, *args):
    return functools.reduce(_prev_intersection, args, a)
intersection.__doc__ = _prev_intersection.__doc__

def difference(a, b, *rest):
    """ Subtracts any number of shapes from the first argument
    """
    return intersection(a, inverse(union(b, *rest)))