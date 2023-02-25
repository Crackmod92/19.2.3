import pytest
from app.calc import Calculator


class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_division_correctly(self):
       assert self.calc.division(self, 2, 2) == 1

   def test_division_failed(self):
       assert self.calc.division(self, 2, 2) == 0