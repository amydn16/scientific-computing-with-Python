import copy
import random

class Hat(object):

    # Hat class takes variable number of arguments
    # Number of balls with certain color
    # Store arguments as the instance variable contents, a list
    def __init__(self, **kwargs):
        contents = []
        # Use keys in dictionary to instantiate objects and fill contents
        for item in kwargs.keys():
            self.__dict__[item] = kwargs[item]
            contents = contents + kwargs[item] * [str(item)]
        self.contents = contents

    # Define draw method to draw a passed number of balls from hat
    def draw(self, number):
        if number > len(self.contents): # Draw more balls than present
            return(self.contents) # Return all balls
        else: # Draw less balls or same number of balls as present 
            drawn = [] # List to store drawn balls
            for i in range(0, number): 
                drawn_ball = random.choice(self.contents) # Draw ball
                drawn = drawn + [drawn_ball] 
                self.contents.remove(drawn_ball) # Remove from hat
        return(drawn)


# Define experiment function to return probability of drawing a color
# hat is Hat object that will be passed into experiment
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # Make a deep copy of hat
    deep_hat = copy.deepcopy(hat)
    
    total = 0 # Number of experiments with expected outcome
    the_balls_drawn = {} # Dictionary to hold balls drawn that are expected

    for item in expected_balls: # Copy keys to the_balls_drawn
        the_balls_drawn[item] = 0 # 0 balls have been drawn

    # For loop to repeat experiments
    for i in range(0, num_experiments):

        # Make a deep copy of deep_hat
        hat = copy.deepcopy(deep_hat)

        # Zero out all entries in the_balls_drawn first
        for item in the_balls_drawn:
            the_balls_drawn[item] = 0

        drawn_list = hat.draw(num_balls_drawn) # List of balls drawn
        # Go through this list to add results to the_balls_drawn
        for item in drawn_list:
            if item in the_balls_drawn:
                the_balls_drawn[item] = the_balls_drawn[item] + 1

        # Check if at least minimum number of desired balls were drawn
        # Use counter to check this condition for all colors
        counter = 0
        for item in the_balls_drawn:
            if the_balls_drawn[item] >= expected_balls[item]:
                counter = counter + 1
        # Check if condition holds for all colors
        if counter == len(expected_balls):
            total = total + 1 # One additional desired outcome

    # Return probability of desired outcome
    return(total / num_experiments)
