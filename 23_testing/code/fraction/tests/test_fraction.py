import pytest
from fraction.fraction import Fraction

class TestFraction:
   def test_fraction_creation(self):
       Fraction(5, 2)
       Fraction(6, 8)
       Fraction(-5, 2)
       Fraction(2, -5)
       Fraction(0, 1)
       Fraction(1, 0)
       Fraction(1, 1)
