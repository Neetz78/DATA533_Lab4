'''This module is for the easy recipes. 
It contains class easy with select,search and display functions. 
The class steps inherits from class easy'''
from recipes.Veg import nutrition as n
class easy:
    ''' The easy class contains 3 functions used to select, search and display the recipe.
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
    nut=""
    ind=0
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
        easy.v=[item for item in input(f"{self.x.I[1],self.x.I[2],self.x.I[3],self.x.I[4],self.x.I[7],self.x.I[8],self.x.I[9],self.x.I[10],self.x.I[11],self.x.I[12],self.x.I[13],self.x.I[14],self.x.I[15],self.x.I[16],self.x.I[18]}:").split()]
        return easy.v


    def search(self):
        '''Searches and promts user to choose dishes from list r and stores the string entered by user in rec
        '''
        for items in easy.v:
            for i in self.x.I:
                if items==i:
                    a=self.x[self.x['I'] == i].index.item()
                    easy.r.append(self.x.R1[a])
                    easy.r.append(self.x.R2[a])
        print("Choose one dish from below choices:\n")
        easy.rec=input(f"{easy.r}:")
        return easy.rec
    
    def display(self):
        ''' Displays the blog and youtube link for the user chosen recipe
        '''
        for i in self.x.R1:
                if easy.rec==i:
                    easy.ind=self.x[self.x['R1'] == i].index.item()
                    print("Recipe blog link: ",self.x.Y1[easy.ind].split(" ")[0], "\n")
                    print("Youtube video link: ",self.x.Y1[easy.ind].split(" ")[1], "\n")
                    return self.x.Y1[easy.ind]

                    
        for i in self.x.R2:
                if easy.rec==i:
                    easy.ind=self.x[self.x['R2'] == i].index.item()
                    print("Recipe blog link: ",self.x.Y2[easy.ind].split(" ")[0], "\n")
                    print("Youtube video link: ",self.x.Y2[easy.ind].split(" ")[1], "\n")
                    return self.x.Y2[easy.ind]
        

                   
    
class steps(easy):
    '''Class for executing the steps. Contains 2 functions
    '''
    def __init__(self,data):
        '''Used to intialize the data with super class
        '''
        easy.__init__(self,data)
    def seasy(self):
        '''Calls the select, search and display functions of the super class.
        Prompts the user if he wants to see the calories and displays the same.'''
        self.select()
        self.search()
        self.display()
        print("Do you want to know the calorie count?\n")
        easy.nut=input("Yes or No")
        if easy.nut=="Yes":
            n.edisplay(self.x,easy.rec,easy.ind)
        else:
            print("Happy cooking!")
    
         
        