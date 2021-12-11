import pandas as pd
import unittest
from unittest.mock import patch
from recipes.NonVeg import difficult as dnv
import recipes.NonVeg.nveg as ve


class TestNonVegDifficult(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestNonVegDifficult.a=dnv.difficult(self.x)
        
    y = "Chicken Egg Fish Lamb Shrimp"
    @patch('builtins.input',return_value=y)
    def test_nonveg_select(self,mock_input):
        
        result1= TestNonVegDifficult.a.select()
        self.assertIn("Chicken", result1)
        self.assertIn("Egg", result1)
        self.assertIn("Fish", result1)
        self.assertIn("Lamb", result1)
        self.assertIn("Shrimp", result1)
   
    
    x=["Devils eggs","Egg Biryani","Chicken Biryani","Chicken lollipop","Sushi","Lebanese fish","Lamb ribs","BBQ Lamb", "Mediterranean shrimp","Shrimp skewers"]
    @patch('builtins.input',return_value=x)
    def test_nonveg_search(self,mock_input):
        
        result2= TestNonVegDifficult.a.search()  
        self.assertIn("BBQ Lamb", result2)
        self.assertIn("Shrimp skewers", result2)
        self.assertIn("Chicken lollipop", result2)
        self.assertIn("Sushi", result2)
        self.assertIn("Lamb ribs", result2)
     

        
    z = ["Easy", "Medium", "Hard", "easy", "medium", "hard", "EASY", "MEDIUM", "HARD", "e", "m" ,"h", "eas", "med", "hrd"]
    @patch('builtins.input',return_value=z)  
    def test_nonveg_level(self,mock_input):
        
        result= ve.level()
        self.assertIn("Hard", result)
        self.assertIn("hard", result)
        self.assertIn("HARD", result)
        self.assertIn("h", result)
        self.assertIn("hrd", result)
        

    
    def tearDown(self):
        print("Tear down")
        
    
    
        


unittest.main(argv=[''], verbosity=2, exit=False)