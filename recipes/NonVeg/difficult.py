'''This module is for the difficult recipes. 
It contains class difficult with select,search and display functions. 
The class steps inherits from class difficult'''

from recipes.NonVeg import nutrition as n
class difficult:
    ''' The difficult class contains 3 functions used to select, search and display the recipe.
    Args:
        v (list): This contains the list of ingredients chosen by the user.
        r (list): Contains recipes names for the ingredients chosen by the user
        rec (str): Contains the recipe of the user chosen dish
        ind (int): Used for fetching index of the dish chosen by the user from the data.
        nut (str): Used for storing if nutrition value is to be displayed.
    '''
    v=[]
    r=[]
    rec=""
    ind=0
    nut=""
    def __init__(self,x):
        '''Initialization function.
        Args:
            x (dataframe): Used for passing the data
        '''
        self.x=x
    def select(self):
        ''' Stores the ungredients chosen by the user in list v
        '''
        print("Please select from the below ingredients:\n")
        difficult.v=[item for item in input(f"{self.x.I[5],self.x.I[0],self.x.I[6],self.x.I[17],self.x.I[19]}:").split()]
        return difficult.v

    
    def search(self):
        '''Searches and promts user to choose dishes from list r and stores the string entered by user in rec
        '''
        for items in difficult.v:
            for i in self.x.I:
                if items==i:
                    a=self.x[self.x['I'] == i].index.item()
                    difficult.r.append(self.x.R5[a])
                    difficult.r.append(self.x.R6[a])
        print("Choose one dish from below choices:\n")
        difficult.rec=input(f"{difficult.r}:")
        if (difficult.rec not in difficult.r):
            print("You did not choose the right dish")
            return difficult.rec
        else:
            return difficult.rec
        
    def display(self):
        ''' Displays the blog and youtube link for the user chosen recipe
        '''
        for i in self.x.R5:
                if difficult.rec==i:
                    difficult.ind=self.x[self.x['R5'] == i].index.item()
                    print("Recipe blog link: ",self.x.Y5[difficult.ind].split(" ")[0], "\n")
                    print("Youtube video link: ",self.x.Y5[difficult.ind].split(" ")[1], "\n")

                    
        for i in self.x.R6:
                if difficult.rec==i:
                    difficult.ind=self.x[self.x['R6'] == i].index.item()
                    print("Recipe blog link: ",self.x.Y6[difficult.ind].split(" ")[0], "\n")
                    print("Youtube video link: ",self.x.Y6[difficult.ind].split(" ")[1], "\n")
        return self.x.Y5[difficult.ind]
                
class steps(difficult):
    '''Class for executing the steps. Contains 2 functions
    '''
    def __init__(self,data):
        '''Used to intialize the data with super class
        '''
        difficult.__init__(self,data)
    def sdiff(self):
        '''Calls the select, search and display functions of the super class.
        Prompts the user if he wants to see the calories and displays the same.'''
        self.select()
        self.search()
        self.display()
        print("Do you want to know the calorie count?\n")        
        try:
            difficult.nut=input("Yes or No")
            if difficult.nut.isdigit():
                raise
            elif difficult.nut not in ["yes", "Yes", "YES", "y", "No","no","n","NO"]:
                raise
        except:
            print("The entered input is invalid")
        finally:
            if difficult.nut in ["yes", "Yes", "YES", "y"]:
                n.ddisplay(self.x,difficult.rec,difficult.ind)
            else:
                print("Happy cooking!")