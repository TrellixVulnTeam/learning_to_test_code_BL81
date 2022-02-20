### NEED 3.11 to use this!!!!


"""
Daily dose of #Python - ep. 5

PEP 673: Self Type

Accepted PEP, will be part of Python 3.11. The main use cases are methods which return instance(s) of their class. This will simplify especially inheritance related usages. Example from the PEP:
"""

from typing import TypeVar
from numpy import isin

"""For after 3.11"""
TShape = TypeVar("TShape", bound="ShapeOld")

class ShapeOld:
    def set_scale(self: TShape, scale: float) -> TShape:
        """Method that returns instance of its class"""
        self.scale = scale
        return self
    
"""This doesnt work? I think need 3.10"""
# class Circle(Shape):
#     def set_radius(self, radius: float) -> Circle:
#         self.radius = radius
#         return self


"""For after 3.11"""
from typing import Self

class Shape:
    def set_scale(self, scale: float) -> Self:
        self.scale = scale
        return self


if __name__ == "__main__":
    #################BEFORE 3.11###########################
    tshape = ShapeOld()
    new_shape = tshape.set_scale(3.22)
    
    print('are above two objects the same type?')
    print(type(tshape) == type(new_shape))
    
    # check type
    print(type(tshape)) # <class '__main__.Shape'>
    print(isinstance(tshape, ShapeOld)) # True
    
    # cannot do this b/c Tshape isnt a type. Its bound to Shape.
    # print(isinstance(tshape, TShape)) # error
    #################BEFORE 3.11###########################
    
    #################AFTER 3.11###########################
    tshape = Shape()
    #################AFTER 3.11###########################