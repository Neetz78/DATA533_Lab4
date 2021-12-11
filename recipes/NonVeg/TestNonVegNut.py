import pandas as pd
import unittest
import sys
import io
import recipes.NonVeg.nutrition as n

class TestNonNutrition(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
    def test_easy_cal(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 
        self.assertEqual(n.edisplay(self.x, "Boiled eggs", 0), 155)
        self.assertEqual(n.edisplay(self.x, "Chicken shawarma", 5), 515)
        self.assertEqual(n.edisplay(self.x, "Pan fried fish", 6), 233)
        self.assertEqual(n.edisplay(self.x, "Oven roasted fish", 6), 131)
        self.assertEqual(n.edisplay(self.x, "Stir fried lamb", 17), 286)
        sys.stdout = sys.__stdout__
        
    def test_medium_cal(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 
        self.assertEqual(n.mdisplay(self.x, "Sunny side up", 0), 70)
        self.assertEqual(n.mdisplay(self.x, "Poached eggs", 0), 143)
        self.assertEqual(n.mdisplay(self.x, "Fish fingers", 6), 249)
        self.assertEqual(n.mdisplay(self.x, "Lamb kabab", 17), 123)
        self.assertEqual(n.mdisplay(self.x, "Lamb curry", 17), 257)
        sys.stdout = sys.__stdout__
        
    def test_diff_cal(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 
        self.assertEqual(n.ddisplay(self.x, "Devils eggs", 0), 200)
        self.assertEqual(n.ddisplay(self.x, "Egg Biryani", 0), 408)
        self.assertEqual(n.ddisplay(self.x, "Chicken Biryani", 5), 400)
        self.assertEqual(n.ddisplay(self.x, "Lebanese fish", 6), 1033)
        self.assertEqual(n.ddisplay(self.x, "Lamb ribs", 17), 670)
        sys.stdout = sys.__stdout__

unittest.main(argv=[''], verbosity=2, exit=False)