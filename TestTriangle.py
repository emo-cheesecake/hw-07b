# -*- coding: utf-8 -*-
"""
Updated April 1, 2026 by Tamara Gonzalez Ibarra
    - Added the following test cases:
        - testRightTriangleC
        - testEquilateralLarge
        - testIsoscelesA/B/C
        - testScaleneA/B
        - testNotTriangleA/B
        - testInvalidTooLarge
        - testInvalidZero/Negative/Float/String
        - testBoundaryMaxValid
        - testBoundaryMinValid

The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk


"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Right Triangle Tests

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(8,15,17),'Right')
    
    # Equilateral Tests
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testEquilateralLarge(self):
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral')
    
    # Isosceles Tests

    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(5,5,3),'Isoceles')

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(5,3,5),'Isoceles')

    def testIsoscelesC(self):
        self.assertEqual(classifyTriangle(3,5,5),'Isoceles')
    
    # Scalene Tests
    
    def testScaleneA(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene')

    def testScaleneB(self):
        self.assertEqual(classifyTriangle(7,8,9),'Scalene')
    
    # Not Triangles Tests
    
    def testNotTriangleA(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle')

    def testNotTriangleB(self):
        self.assertEqual(classifyTriangle(10,1,1),'NotATriangle')
    
    # Invalid Inputs
    
    def testInvalidTooLarge(self):
        self.assertEqual(classifyTriangle(201,10,10),'InvalidInput')

    def testInvalidZero(self):
        self.assertEqual(classifyTriangle(0,10,10),'InvalidInput')

    def testInvalidNegative(self):
        self.assertEqual(classifyTriangle(-1,10,10),'InvalidInput')
    
    def testInvalidFloat(self):
        self.assertEqual(classifyTriangle(3.5,4,5),'InvalidInput')

    def testInvalidString(self):
        self.assertEqual(classifyTriangle("3",4,5),'InvalidInput')
    
    # Boundary Tests
    
    def testBoundaryMaxValid(self):
        self.assertEqual(classifyTriangle(200,199,199),'Isoceles')

    def testBoundaryMinValid(self):
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

