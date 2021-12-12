'''This module is for the intermediate recipes. 
It contains class medium with select,search and display functions. 
The class steps inherits from class medium'''
from recipes.Veg import nutrition as n
class medium:
    ''' The medium class contains 3 functions used to select, search and display the recipe.
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
        medium.v=[item for item in input(f"{self.x.I[1],self.x.I[2],self.x.I[3],self.x.I[4],self.x.I[7],self.x.I[8],self.x.I[9],self.x.I[10],self.x.I[11],self.x.I[12],self.x.I[13],self.x.I[14],self.x.I[15],self.x.I[16],self.x.I[18]}:").split()]
        return medium.v
    
    def search(self):
        '''Searches and promts user to choose dishes from list r and stores the string entered by user in rec
        '''
        for items in medium.v:
            for i in self.x.I:
                if items==i:
                    a=self.x[self.x['I'] == i].index.item()
                    medium.r.append(self.x.R3[a])
                    medium.r.append(self.x.R4[a])
        print("Choose one dish from below choices:\n")
        medium.rec=input(f"{medium.r}:")
        return medium.rec
    
    def display(self):
        ''' Displays the blog and youtube link for the user chosen recipe
        '''
        for i in self.x.R3:
                if medium.rec==i:
                    medium.ind=self.x[self.x['R3'] == i].index.item()
                    print("Recipe blog link: ",self.x.Y3[medium.ind].split(" ")[0], "\n")
                    print("Youtube video link: ",self.x.Y3[medium.ind].split(" ")[1], "\n")

                    
        for i in self.x.R4:
                if medium.rec==i:
                    medium.ind=self.x[self.x['R4'] == i].index.item()
                    print("Recipe blog link: ",self.x.Y4[medium.ind].split(" ")[0], "\n")
                    print("Youtube video link: ",self.x.Y4[medium.ind].split(" ")[1], "\n")
        return self.x.Y4[medium.ind]
                    
                   
    
    
class steps(medium):
    '''Class for executing the steps. Contains 2 functions
    '''
    def __init__(self,data):
        '''Used to intialize the data with super class
        '''
        medium.__init__(self,data)
    def smedium(self):
        '''Calls the select, search and display functions of the super class.
        Prompts the user if he wants to see the calories and displays the same.
        '''
        self.select()
        self.search()
        self.display()
        print("Do you want to know the calorie count?\n")
        try:
            medium.nut=input("Yes or No")
            if medium.nut.isdigit():
                raise
            elif medium.nut not in ["yes", "Yes", "YES", "y", "No","no","n","NO"]:
                raise
        except:
            print("The entered input is invalid")
        finally:
            if medium.nut in ["yes", "Yes", "YES", "y"]:
                n.mdisplay(self.x,medium.rec,medium.ind)
            else:
                print("Happy cooking!")