import pandas as pd
import unittest
from unittest.mock import patch
from DNRecipe.NonVeg import difficult as dnv
import DNRecipe.NonVeg.nveg as ve


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
        TestNonVegDifficult.b=dnv.steps(self.x)
        
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
        
        self.assertIn("Devils eggs", result2)
        self.assertIn("Chicken lollipop", result2)
        self.assertIn("Lebanese fish", result2)
        self.assertIn("Lamb ribs", result2)
        self.assertIn("Mediterranean shrimp", result2)
     

        
    z = ["Easy", "Medium", "Hard", "easy", "medium", "hard", "EASY", "MEDIUM", "HARD", "e", "m" ,"h", "eas", "med", "hrd"]
    @patch('builtins.input',return_value=z)  
    def test_nonveg_level(self,mock_input):
        
        result= ve.level()
        self.assertIn("Hard", result)
        self.assertIn("hard", result)
        self.assertIn("HARD", result)
        self.assertIn("h", result)
        self.assertIn("hrd", result)
        
    k = ["https://www.foodnetwork.com/recipes/classic-deviled-eggs-recipe-1911032 https://www.youtube.com/watch?v=KmzbiuW4r1I"]
    @patch('builtins.input',return_value=k)  
    def test_nonveg_display(self,mock_input):
        
        result3= TestNonVegDifficult.a.display() 
        self.assertIn("https://www.foodnetwork.com/recipes/classic-deviled-eggs-recipe-1911032 https://www.youtube.com/watch?v=KmzbiuW4r1I", result3)
        
    l = "yes Yes YES y No no n NO"
    @patch('builtins.input',return_value=l)  
    def test_nonveg_sdiff(self,mock_input):
        
        result4= TestNonVegDifficult.b.sdiff() 
        self.assertIn("Yes", result4)
        
    def tearDown(self):
        print("Tear down")
unittest.main(argv=[''], verbosity=2, exit=False)