import pandas as pd
import unittest
from unittest.mock import patch
from DNRecipe.NonVeg import intermediate as mnv
import DNRecipe.NonVeg.nveg as ve

class TestNonVegMedium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestNonVegMedium.a=mnv.medium(self.x)
        TestNonVegMedium.b=mnv.steps(self.x)
    y = "Chicken Eggs Fish Lamb Shrimp"
    @patch('builtins.input',return_value=y)
    def test_nonveg_select(self,mock_input):

        result1= TestNonVegMedium.a.select()
        
        self.assertIn("Chicken", result1)
        self.assertIn("Eggs", result1)
        self.assertIn("Fish", result1)
        self.assertIn("Lamb", result1)
        self.assertIn("Shrimp", result1)

        
    
    x=["Sunny side up","Poached eggs","Barbeque chicken","Chicken gravy","Fish fingers","Fish gravy","Lamb curry","Lamb kabab","Honey garlic shrimp","Shrimp dip"]
    @patch('builtins.input',return_value=x)
    def test_nonveg_search(self,mock_input):
        result2= TestNonVegMedium.a.search()
        
        self.assertIn("Poached eggs", result2)
        self.assertIn("Barbeque chicken", result2)
        self.assertIn("Chicken gravy", result2)
        self.assertIn("Fish gravy", result2)
        self.assertIn("Shrimp dip", result2)
        
    z = ["Easy", "Medium", "Hard", "easy", "medium", "hard", "EASY", "MEDIUM", "HARD", "e", "m" ,"h", "eas", "med", "hrd"]
    @patch('builtins.input',return_value=z)
        
    def test_nonveg_level(self,mock_input):
        result= ve.level()
        self.assertIn("Medium", result)
        self.assertIn("m", result)
        self.assertIn("MEDIUM", result)
        self.assertIn("medium", result)
        self.assertIn("med", result)
        
    k = ["https://www.cookinglight.com/recipes/pristine-sunny-side-up-eggs https://www.youtube.com/watch?v=hS0AEh8fxiM"]
    @patch('builtins.input',return_value=k)  
    def test_nonveg_display(self,mock_input):
        
        result3= TestNonVegMedium.a.display() 
        self.assertIn("https://www.cookinglight.com/recipes/pristine-sunny-side-up-eggs https://www.youtube.com/watch?v=hS0AEh8fxiM", result3)
        
    l = "yes Yes YES y No no n NO"
    @patch('builtins.input',return_value=l)  
    def test_nonveg_smedium(self,mock_input):
        
        result4= TestNonVegMedium.b.smedium() 
        self.assertIn("Yes", result4)
        
    def tearDown(self):
        print("Tear down")
        
unittest.main(argv=[''], verbosity=2, exit=False)