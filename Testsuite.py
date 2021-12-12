import unittest
from DNRecipe.Veg.TestVegNut import TestNutrition  
from DNRecipe.NonVeg.TestNonVegNut import TestNonNutrition 
from DNRecipe.Veg.TestVegEasy import TestVegEasy 
from DNRecipe.NonVeg.TestNonVegEasy import TestNonVegEasy 
from DNRecipe.Veg.TestVegMedium import TestVegMedium 
from DNRecipe.NonVeg.TestNonVegMedium import TestNonVegMedium 
from DNRecipe.Veg.TestVegDiff import TestVegDifficult 
from DNRecipe.NonVeg.TestNonVegDifficult import TestNonVegDifficult


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult() 
    suite.addTest(unittest.makeSuite(TestNutrition)) 
    suite.addTest(unittest.makeSuite(TestNonNutrition))
    suite.addTest(unittest.makeSuite(TestVegEasy))
    suite.addTest(unittest.makeSuite(TestNonVegEasy))
    suite.addTest(unittest.makeSuite(TestVegMedium))
    suite.addTest(unittest.makeSuite(TestNonVegMedium))
    suite.addTest(unittest.makeSuite(TestVegDifficult))
    suite.addTest(unittest.makeSuite(TestNonVegDifficult))
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
my_suite()