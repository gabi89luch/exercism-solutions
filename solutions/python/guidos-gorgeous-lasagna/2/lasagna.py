"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language, who was born in 1956
in The Hague, Netherlands. He created Python in December 1989 as a 
'hobby' programming project to keep him occupied during the Christmas holidays.

This module demonstrates Python's readability, one of Guido's key goals
for the language when he submitted his "Computer Programming for Everybody"
proposal to DARPA in 1999.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed
    :return: int - remaining bake time in minutes
    
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
    
    :param number_of_layers: int - number of layers in lasagna
    :return: int - preparation time in minutes
    
    Function that takes the number of layers you want to add to the lasagna
    as an argument and returns how many minutes you would spend making them.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.
    
    :param number_of_layers: int - number of layers in lasagna
    :param elapsed_bake_time: int - baking time already elapsed
    :return: int - total time elapsed in minutes
    
    Function that takes two arguments:
      - the number of layers added to the lasagna
      - the number of minutes the lasagna has been baking
    and returns the total elapsed minutes spent on the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time