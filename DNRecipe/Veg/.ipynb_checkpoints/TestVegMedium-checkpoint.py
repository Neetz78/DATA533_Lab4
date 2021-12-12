import pandas as pd
import unittest
from unittest.mock import patch
from DNRecipe.Veg import intermediate as mv
import DNRecipe.Veg.veg as nve

class TestVegMedium(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestVegMedium.a=mv.medium(self.x)
        TestVegMedium.b=mv.steps(self.x)

    y = "Bread Milk Flour Rice Carrot Potato Brocolli Onion Cheese Oats Lentils Noodles Pasta Corn Spinach"
    @patch('builtins.input',return_value=y)
    def test_veg_select(self,mock_input):

        result1= TestVegMedium.a.select()
        
        self.assertIn("Onion", result1)
        self.assertIn("Oats", result1)
        self.assertIn("Rice", result1)
        self.assertIn("Noodles", result1)
        self.assertIn("Corn", result1)
    
    x=["Sandwich","Hot chocolate","Bread","Veg Sushi","Carrot paratha","French fries","Pasta","Onion rings","Mozerella Cheese sticks","Oats Upma", "Indian Dal","Chopsuey","Arabiata pasta","Corn and cheese","Spinach paratha","Bread Manchurian","Milk Shake","Crepes","Fried rice","Carrot soup","Twisted potato","Brocolli paratha","Cheesy Onions","Cheese cake","Health bar","Dal soup","Fried noodles","White sauce pasta","Corn Crackers","Palak paneer"]
    @patch('builtins.input',return_value=x)
    def test_veg_search(self,mock_input):
        result2= TestVegMedium.a.search()
        
        self.assertIn("Sandwich", result2)
        self.assertIn("Bread", result2)
        self.assertIn("Corn and cheese", result2)
        self.assertIn("Fried noodles", result2)
        self.assertIn("White sauce pasta", result2)
    z = ["Easy", "Medium", "Hard", "easy", "medium", "hard", "EASY", "MEDIUM", "HARD", "e", "m" ,"h", "eas", "med", "hrd"]
    @patch('builtins.input',return_value=z)
        
    def test_veg_level(self,mock_input):
        result= nve.level()
        self.assertIn("Medium", result)
        self.assertIn("m", result)
        self.assertIn("MEDIUM", result)
        self.assertIn("medium", result)
        self.assertIn("med", result)
        
    k = ["https://downshiftology.com/recipes/poached-eggs/ https://www.youtube.com/watch?v=yifZtA3uF-E"]
    @patch('builtins.input',return_value=k)  
    def test_veg_display(self,mock_input):
        
        result3= TestVegMedium.a.display() 
        self.assertIn("https://downshiftology.com/recipes/poached-eggs/ https://www.youtube.com/watch?v=yifZtA3uF-E", result3)
    
    l = "yes Yes YES y No no n NO"
    @patch('builtins.input',return_value=l)  
    def test_veg_smedium(self,mock_input):
        
        result4= TestVegMedium.b.smedium() 
        self.assertIn("Yes", result4)
    
    def tearDown(self):
        print("Tear down")
        
unittest.main(argv=[''], verbosity=2, exit=False)