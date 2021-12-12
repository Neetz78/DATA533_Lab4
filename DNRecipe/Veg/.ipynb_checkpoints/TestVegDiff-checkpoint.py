import pandas as pd
import unittest
from unittest.mock import patch
from DNRecipe.Veg import difficult as ev
import DNRecipe.Veg.veg as nve

class TestVegDifficult(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestVegDifficult.a=ev.difficult(self.x)
        TestVegDifficult.b=ev.steps(self.x)
    y = "Bread Milk Flour Rice Carrot Potato Brocolli Onion Cheese Oats Lentils Noodles Pasta Corn Spinach"
    @patch('builtins.input',return_value=y)
    def test_veg_select(self,mock_input):

        result1= TestVegDifficult.a.select()
        
        self.assertIn("Bread", result1)
        self.assertIn("Flour", result1)
        self.assertIn("Rice", result1)
        self.assertIn("Potato", result1)
        self.assertIn("Lentils", result1)
    
    x=["Bread pakoda","Rabdi","Tacos","Veg Biryani","Carrot Cake","Aloo paratha","Brocolli manchurian","French onion soup","Corn and cheese momos","Oats pancake","Dal paratha","Wonton noodle soup","Lasagna","Corn pakoda","Spinach ravioli","Bread Upma","Kulfi","Muffins","Dosa","Carrot halwa","Cajun spiced potato","Brocolli base pizza","Onion paratha","Cheesy Pizza","Oats cookie","Dal pakoda","Veggie garlic noodles","Ravioli pasta","Corn soup","Spinach chaat"]
    @patch('builtins.input',return_value=x)
    def test_veg_search(self,mock_input):
        result2= TestVegDifficult.a.search()
        
        self.assertIn("Bread pakoda", result2)
        self.assertIn("Spinach ravioli", result2)
        self.assertIn("Oats pancake", result2)
        self.assertIn("Ravioli pasta", result2)
        self.assertIn("Spinach chaat", result2)
        
    z = ["Easy", "Medium", "Hard", "easy", "medium", "hard", "EASY", "MEDIUM", "HARD", "e", "m" ,"h", "eas", "med", "hrd"]
    @patch('builtins.input',return_value=z)
        
    def test_veg_level(self,mock_input):
        result= nve.level()
        self.assertIn("Hard", result)
        self.assertIn("hard", result)
        self.assertIn("HARD", result)
        self.assertIn("h", result)
        self.assertIn("hrd", result)

    k = ["https://www.indianhealthyrecipes.com/egg-biryani-recipe-how-to-make-easy-egg-biryani/ https://www.youtube.com/watch?v=5VapbxkA_UA"]
    @patch('builtins.input',return_value=k)  
    def test_veg_display(self,mock_input):
        
        result3= TestVegDifficult.a.display() 
        self.assertIn("https://www.indianhealthyrecipes.com/egg-biryani-recipe-how-to-make-easy-egg-biryani/ https://www.youtube.com/watch?v=5VapbxkA_UA", result3)
        
        
    l = "yes Yes YES y No no n NO"
    @patch('builtins.input',return_value=l)  
    def test_veg_sdiff(self,mock_input):
        
        result4= TestVegDifficult.b.sdiff() 
        self.assertIn("Yes", result4)
    def tearDown(self):
        print("Tear down")

        
unittest.main(argv=[''], verbosity=2, exit=False)