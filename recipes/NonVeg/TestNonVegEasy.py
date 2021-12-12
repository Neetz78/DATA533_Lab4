import pandas as pd
import unittest
from unittest.mock import patch
from recipes.NonVeg import easy as env
import recipes.NonVeg.nveg as ve

class TestNonVegEasy(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestNonVegEasy.a=env.easy(self.x)
    y = "Chicken Egg Fish Lamb Shrimp"
    @patch('builtins.input',return_value=y)
    def test_nonveg_select(self,mock_input):

        result1= TestNonVegEasy.a.select()
        
        self.assertIn("Chicken", result1)
        self.assertIn("Egg", result1)
        self.assertIn("Fish", result1)
        self.assertIn("Lamb", result1)
        self.assertIn("Shrimp", result1)

    
    x=["Boiled eggs","Scrambled eggs","Pan tossed chicken","Chicken shawarma","Pan fried fish","Oven roasted fish","Stir fried lamb","Baked lamb","Party Shrimp", "Garlic Shrimp stir fry" ]
    @patch('builtins.input',return_value=x)
    def test_nonveg_search(self,mock_input):
        result2= TestNonVegEasy.a.search()
        
        self.assertIn("Boiled eggs", result2)
        self.assertIn("Chicken shawarma", result2)
        self.assertIn("Oven roasted fish", result2)
        self.assertIn("Stir fried lamb", result2)
        self.assertIn("Party Shrimp", result2)
        
    z = ["Easy", "Medium", "Hard", "easy", "medium", "hard", "EASY", "MEDIUM", "HARD", "e", "m" ,"h", "eas", "med", "hrd"]
    @patch('builtins.input',return_value=z)
        
    def test_nonveg_level(self,mock_input):
        result= ve.level()
        self.assertIn("Easy", result)
        self.assertIn("easy", result)
        self.assertIn("EASY", result)
        self.assertIn("e", result)
        self.assertIn("eas", result)
    
    k = ["https://www.simplyrecipes.com/recipes/how_to_make_perfect_hard_boiled_eggs/ https://www.youtube.com/watch?v=3CnAQzEiuvQ"]
    @patch('builtins.input',return_value=k)  
    def test_nonveg_display(self,mock_input):
        
        result3= TestNonVegEasy.a.display() 
        self.assertIn("https://www.simplyrecipes.com/recipes/how_to_make_perfect_hard_boiled_eggs/ https://www.youtube.com/watch?v=3CnAQzEiuvQ", result3)
        
    def tearDown(self):
        print("Tear down")
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


        
unittest.main(argv=[''], verbosity=2, exit=False)