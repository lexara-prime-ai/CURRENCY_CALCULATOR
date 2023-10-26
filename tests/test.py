import unittest
import app


class AppTestCase(unittest.TestCase):
    def test_rate_values(self):
        self.assertEqual(app.rates.get("usd"), 150.20)
        self.assertEqual(app.rates.get("euro"), 180.0)


if __name__ == '__main__':
    unittest.main()
