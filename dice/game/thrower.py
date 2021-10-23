import random

# TODO: Define the Thrower class here.
class Thrower():
    ''' -The thrower is the person who throws all the dice at the beginning of each turn
        -This class say when the person can throw, it throws the dice and says the points that he gets

        Attributes:
        dice: are the dice values
        
    '''
    def __init__(self):   #-------------initialize attributes

        self.dice = []
        self.num_throws = 0
        pass

    def can_throw(self): #---------say if the thrower can throws the dice, retrun true if there is a five or a one or a zero
        
        return(self.dice.count(5)>0 or self.dice.count(1)>0 or self.num_throws == 0)
        pass

    def get_points(self):#---------calculate the points

        return self.dice.count(5)*50 + self.dice.count(1)*100
        pass

    def throw_dice(self): #----------generate ranbom values

        self.dice.clear()

        for d in range(5):
            value = random.randint(1,6)
            self.dice.append(value)
        self.num_throws += 1
        pass