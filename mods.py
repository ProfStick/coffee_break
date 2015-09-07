""" Project name.

Description
"""

__copyright__ = "(c) Geoff Goldrick 2014"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Geoff Goldrick"
__version__ = "1.0"
__revision__ = "20150907"

""" revision notes:


"""

#dependencies
import pygame as P
import random as R

class Cup(object):
    """coffee cup.

    Create a coffee cup with necessary parameters to draw it

    Attributes:
        screen_size: the size of the display screen in pixels

    """

    def __init__(self,screen_size, now, max_rate=5):
        """Inits Cup."""
        self.image = P.image.load('images/coffee_cup_hot.png')
        self.x = R.randrange(screen_size[0]-50) #image width is 50
        self.y = 0
        self.rectangle = self.image.get_rect().move(self.x,self.y)
        self.created = now
        self.temp = "hot"
        self.move_rate = R.randrange(1,max_rate)



    def update(self,time_now, screen_size):
        """Performs operation blah."""
        self.rectangle = self.rectangle.move(0,self.move_rate)
        if time_now - self.created > 10000:
            self.image = P.image.load('images/coffee_cup_cold.png')
            self.temp = "cold"
        elif time_now - self.created > 7500:
            self.image = P.image.load('images/coffee_cup_cool.png')
            self.temp = 'cool'
        elif time_now - self.created > 5000:
            self.image = P.image.load('images/coffee_cup_lukewarm.png')
            self.temp = "lukewarm"
        elif time_now - self.created > 2500:
            self.image = P.image.load('images/coffee_cup_warm.png')
            self.temp = "warm"

        if self.rectangle.bottom > screen_size[1]:
            self.image = P.image.load('images/coffee_cup_cracked.png')
            self.temp = "cold"





def function_name(arg1, arg2, other_silly_variable=None):
    """Does something amazing.

    a much longer description of the really amazing stuff this function does and how it does it.

    Args:
        arg1: the first argument required by the function.
        arg2: the second argument required by the function.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        description of the stuff that is returned by the function.

    Raises:
        AnError: An error occurred running this function.
    """
    pass

class SampleClass(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""



