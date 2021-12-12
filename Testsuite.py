import unittest
from recipes.Veg.TestVegNut import TestNutrition  
from recipes.NonVeg.TestNonVegNut import TestNonNutrition 
from recipes.Veg.TestVegEasy import TestVegEasy 
from recipes.NonVeg.TestNonVegEasy import TestNonVegEasy 
from recipes.Veg.TestVegMedium import TestVegMedium 
from recipes.NonVeg.TestNonVegMedium import TestNonVegMedium 
from recipes.Veg.TestVegDiff import TestVegDifficult 
from recipes.NonVeg.TestNonVegDifficult import TestNonVegDifficult


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