import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):

    def test_can_create_0_fraction_from_str(self):
        frac = Fraction.from_string('0')
        self.assertTrue(frac.is_equal(0, 1))


class TestFractionOperations(unittest.TestCase):
    def test_sum_fraction_1_2_1_2(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(1, 1))

    def test_s_fraction_1_2_minus_1_2(self):
        frac_1 = Fraction(1, 2)
        frac_2 = Fraction(-1, 2)
        result = frac_1 + frac_2
        self.assertTrue(result.is_equal(0, 1))
