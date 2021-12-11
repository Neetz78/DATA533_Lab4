def edisplay(x,r,a):
    ''' Displays the calorie count for easy dishes.
    Args:
        x (data.frame): Contains the given data
        r (str): Dish selected by the user
        a (int): Contains the index from the data for the dish selected by the user.
    '''
    if x.R1[a] == r:
        print("Calorie count:",x.C1[a],"\n")
        return x.C1[a]
    elif x.R2[a] == r:
        print("Calorie count:",x.C2[a],"\n")
        return x.C2[a]
def mdisplay(x,r,a):
    ''' Displays the calorie count for medium dishes.
    Args:
        x (data.frame): Contains the given data
        r (str): Dish selected by the user
        a (int): Contains the index from the data for the dish selected by the user.
    '''
    if x.R3[a] == r:
        print("Calorie count:",x.C3[a],"\n")
        return x.C3[a]
    elif x.R4[a] == r:
        print("Calorie count:",x.C4[a],"\n")
        return x.C4[a]
def ddisplay(x,r,a):
    ''' Displays the calorie count for difficult dishes.
    Args:
        x (data.frame): Contains the given data
        r (str): Dish selected by the user
        a (int): Contains the index from the data for the dish selected by the user.
    '''
    if x.R5[a] == r:
        print("Calorie count:",x.C5[a],"\n")
        return x.C5[a]
    elif x.R6[a] == r:
        print("Calorie count:",x.C6[a],"\n")
        return x.C6[a]