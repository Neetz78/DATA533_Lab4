import pandas as pd
import unittest
from unittest.mock import patch
from recipes.Veg import easy as ev
import recipes.Veg.veg as nve

class TestVegEasy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestVegEasy.a=ev.easy(self.x)
    y = "Bread Milk Flour Rice Carrot Potato Brocolli Onion Cheese Oats Lentils Noodles Pasta Corn Spinach"
    @patch('builtins.input',return_value=y)
    def test_veg_select(self,mock_input):

        result1= TestVegEasy.a.select()
        
        self.assertIn("Bread", result1)
        self.assertIn("Flour", result1)
        self.assertIn("Rice", result1)
        self.assertIn("Potato", result1)
        self.assertIn("Lentils", result1)
    
    x=["Butter toast", "Coffee", "Roti", "Flavoured rice" , "Carrot Salad", "Mashed potato", "Brocolli Salad", "Onion Salad", "Mac and cheese", "Overnight soaked oats", "Sprouts", "Chinese noodles", "Pasta salad", "Baked corn", "Spinach and corn", "Garlic bread", "Tea", "Pancakes", "Porridge", "Stir fried carrot", "Potato wedges", "Stir fried brocolli", "Sauted onions", "Cheese toast", "Smoothie", "Khichdi", "Noodle soup", "Pasta chips", "Popcorn", "Spinach soup"]
    @patch('builtins.input',return_value=x)
    def test_veg_search(self,mock_input):
        result2= TestVegEasy.a.search()
        
        self.assertIn("Flavoured rice", result2)
        self.assertIn("Roti", result2)
        self.assertIn("Carrot Salad", result2)
        self.assertIn("Garlic bread", result2)
        self.assertIn("Flavoured rice", result2)
    z = ["Easy", "Medium", "Hard", "easy", "medium", "hard", "EASY", "MEDIUM", "HARD", "e", "m" ,"h", "eas", "med", "hrd"]
    @patch('builtins.input',return_value=z)
        
    def test_veg_level(self,mock_input):
        result= nve.level()
        self.assertIn("Easy", result)
        self.assertIn("easy", result)
        self.assertIn("EASY", result)
        self.assertIn("e", result)
        self.assertIn("eas", result)
        
    def tearDown(self):
        print("Tear down")

        
unittest.main(argv=[''], verbosity=2, exit=False)