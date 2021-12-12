# DATA533_Lab2
# Disha and Neethu
## Recipes package
## Recipes csv file uploaded.

* The recipes package contains a program that displays the recipe and the calories of that particular dish.
* The recipe of the dish displayed is based on the ingredients chosen by the user.
    * Step 1: User is asked to choose between Non-Vegetarian and Vegetarian.
    * Step 2: User is asked choose from the difficulty level of cooking : Easy, Medium or Hard.
    * Step 3: The user is presented a list of ingredients.
    * Step 4: User has to enter the ingredients he wishes.
    * Step 5: A list of recipes based on the user entered ingredients is displayed. 
    * Step 6: The user is asked to choose from the list of recipes mentioned.
    * Step 7: The selected recipe blog link and the corresponding youtube link for the recipe is displayed to the user.
    * Step 8: The program also prompts if the user wants to know the calories of that particular recipe.
    * Step 9: If the user enters yes, the calorie count of the dish selected is displayed.

* The main package is recipes which contains which contains two sub packages Veg and Non-Veg. It also contains an initialization file and a module called recipe.
    * The recipe module contains the the code for execution of the package.
* The sub packages each have six modules:
    * Module veg and nonveg are used to take the level of difficulty from the user.
    * Modules easy,intermediate and difficult are used to define the difficulty level of the recipes.
        * Each of these modules contain easy,medium and difficult classes respectively. These classes have the following functions:
            * select(): This function is used to prompt the user to select the ingredients from the given list.
            * search(): This function searches the predefined data for the ingredients chosen by the user. It matches the ingredients with the dataset and displays the names of the dishes for the corresponding ingredients.
            * display(): This function displays the recipe blog link and the youtube video link for the user chosen dish.
        * Class steps is a subclass inhereting features from corresponding easy, medium or difficult super classes. This has the following function:
            * seasy(),smedium(),sdiff() for the classes easy, medium and difficult respectively which calls the function from the respective super class to select,search and display.
    * Module nutrition displays the calorie count of the user chosen dish
* The csv file Recipe.csv contains a list of ingredients and the recipe ideas for the ingredients with recipe links and calorie values for each dish.
* The Code.ipynb is the main file which imports recipes package and calls the function recipe using it..

