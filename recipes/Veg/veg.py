class VegError(Exception):
    pass
class LevelIsNumber(VegError):
    pass
class LevelIsInvalid(VegError):
    pass

'''Module for taking user input for vegetarian recipes'''
def level():
    '''Returns the level of difficulty selected by the user
    '''
    print("Choose the difficulty level\n")
    try:
        level = input("Easy , Medium , Hard:")
        
        if level.isdigit():
            raise LevelIsNumber()
        elif level not in ["Easy","easy","e","EASY","eas","Medium","medium","m","MEDIUM","med","Hard","hard","h","HARD","hrd"]:
            raise LevelIsInvalid()
        
    except LevelIsNumber:
        print("The level entered is a number. Kindly re-enter.")
    except LevelIsInvalid:
        print("Please enter a valid preference. Kindly re-enter.")
    finally:
        return level
        
    
    
    

    
    