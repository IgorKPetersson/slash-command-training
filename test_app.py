import unittest

from app import calculate_total


class TestCalculateTotal(unittest.TestCase):

    def test_regular_customer(self):
        self.assertEqual(
            calculate_total(100, 2, "regular"),
            200,
        )

    def test_premium_customer(self):
        self.assertEqual(
            calculate_total(100, 2, "premium"),
            180,
        )

    def test_vip_customer(self):
        self.assertEqual(
            calculate_total(100, 2, "vip"),
            160,
        )

    def test_quantity_must_be_positive(self):
        with self.assertRaises(ValueError):
            calculate_total(100, 0, "regular")

    def test_price_must_be_positive(self):
        with self.assertRaises(ValueError):
            calculate_total(0, 2, "regular")


if __name__ == "__main__":
    unittest.main()