import pytest
from app.calc import Calculator


class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_adding_correctly(self):
       assert self.calc.adding(self, 2, 2) == 4

   def test_adding_failed(self):
       assert self.calc.adding(self, 2, 2) == 3