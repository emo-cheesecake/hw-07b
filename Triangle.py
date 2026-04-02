# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated April 1, 2026 by Tamara Gonzalez Ibarra

The primary goal of this file is to demonstrate a simple python program to classify triangles

"""

def classifyTriangle(a,b,c):
    """
    Updated code
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
    """
    # Prevents TypeErrors
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # Range check 
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Triangle inequality (correct logic)
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Right triangle check
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'

    # Equilateral
    if a == b == c:
        return 'Equilateral'

    # Isosceles
    if a == b or b == c or a == c:
        return 'Isoceles'

    # Scalene
    return 'Scalene'  