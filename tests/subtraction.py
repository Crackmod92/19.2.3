import pytest
from app.calc import Calculator


class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_subtraction_calculate_correctly(self):
       assert self.calc.subtraction(self, 2, 2) == 0

   def test_subtraction_failed(self):
       assert self.calc.subtraction(self, 2, 2) == 1