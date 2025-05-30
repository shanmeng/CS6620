Name: Shan Meng
Date: May 29, 2025
Class: CS6620, Summer
Notes: CI/CD Pipeline Part 1




import unittest
from packer import suggest_items

class TestSmartPacker(unittest.TestCase):
    def test_basic_trip(self):
        result = suggest_items("Paris", 2)
        self.assertEqual(result["clothes"].count("shirt"), 2)
        self.assertIn("phone charger", result["electronics"])

    def test_beach_destination(self):
        result = suggest_items("Bali", 3)
        self.assertIn("sunscreen", result["extras"])

    def test_cold_weather(self):
        result = suggest_items("Toronto", 1, weather="cold")
        self.assertIn("jacket", result["clothes"])
        self.assertIn("gloves", result["clothes"])

    def test_rainy_weather(self):
        result = suggest_items("Seattle", 2, weather="rain")
        self.assertIn("umbrella", result["extras"])

    def test_with_kids(self):
        result = suggest_items("London", 3, with_kids=True)
        self.assertIn("diapers (1 pack/day)", result["kids"])
        self.assertGreaterEqual(len(result["kids"]), 5)

    def test_with_pet(self):
        result = suggest_items("New York", 2, with_pet=True)
        self.assertIn("pet food", result["pet"])
        self.assertGreaterEqual(len(result["pet"]), 5)

if __name__ == "__main__":
    unittest.main()