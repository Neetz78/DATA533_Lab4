class Error(Exception):
    pass
class InputIsNumberError(Error):
    pass
class InputInvalidError(Error):
    pass
def recipe():
    
    '''The recipe package
     Importing all the required modules for execution
     Imports pandas,recipes.Veg.veg,recipes.NonVeg.nveg,recipes.Veg,recipes.NonVeg modules
     
     Parameters:
     
     data(Dataframe) : Consists of the recipe book.
     
     perf(Str) : Contians the food preference of the user.
     
     lev,nlev(Str) : It takes the difficulty level entered by the user
     
     a(class object) : An class object to call the respective easy, medium or difficult methods.
     
     
     '''
    
    import pandas as pd
    import recipes.Veg.veg as veg
    import string
    import recipes.NonVeg.nveg as nveg
    from recipes.Veg import easy as e,intermediate as i,difficult as d 
    from recipes.NonVeg import easy as ne,intermediate as ni,difficult as nd
    
    

    data = pd.read_csv("Recipes.csv",encoding = "ISO-8859-1", engine='python')

    print("Please select your food preference or type x to exit")
    
    try:
        perf = input("Vegetarian or Non-Vegetarian:")
        
        if perf.isdigit():
            raise InputIsNumberError()
        elif perf not in ["Vegetarian","Veg","veg","vegetarian","Non-Vegetarian","Non-Veg","nonveg","nonvegetarian" ,"NonVegetarian","Nonveg", "x"]:
            raise InputInvalidError()
        
    except InputIsNumberError:
        print("The preference entered is a number. Kindly re-enter or type x to exit")
    except InputInvalidError:
        print("Please enter a valid preference. Kindly re-enter or type x to exit")
        
        
    else:
        
        if (perf == "Vegetarian" or perf == "Veg" or perf == "veg" or perf == "vegetarian"):
            lev = veg.level()
            if (lev == "Easy" or lev == "easy" or lev == "e" or lev == "EASY" or lev=="eas"):
                a=e.steps(data)
                a.seasy()
            elif (lev == "Medium" or lev == "medium" or lev == "m" or lev == "MEDIUM" or lev== "med"):
                a=i.steps(data)
                a.smedium()
            elif (lev == "Hard" or lev == "hard" or lev == "h" or lev == "HARD" or lev=="hrd"):
                a=d.steps(data)
                a.sdiff()
            else:
                pass
    
        elif (perf == "Non-Vegetarian" or perf == "Non-Veg" or perf == "nonveg" or perf == "nonvegetarian" or perf == "NonVegetarian" or perf == "Nonveg"):
            nlev = nveg.level()
            if (nlev == "Easy" or nlev == "easy" or nlev == "e" or nlev == "EASY" or nlev=="eas"):
                a=ne.steps(data)
                a.seasy()
            elif (nlev == "Medium" or nlev == "medium" or nlev == "m" or nlev == "MEDIUM"or nlev== "med"):
                a=ni.steps(data)
                a.smedium()
            elif (nlev == "Hard" or nlev == "hard" or nlev == "h" or nlev == "HARD" or nlev=="hrd"):
                a=nd.steps(data)
                a.sdiff()
            else:
                pass
        else:
            pass
        
    finally:
        if perf != "x":
            recipe()
    
    





