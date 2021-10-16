import random
import copy

def deck():
    """
    () -> list
    Returns a deck of cards as a list. Each element in the list is a list of a string representing the suit ("spades", "clubs", "diamonds", or "hearts" and an integer representing the number of the card (1 to 13). 
    """
    family = ['spades','clubs','diamonds','hearts']
    deck = []
    for i in family:
         for j in range(1,14):
            card = [i,j]
            deck.append(card)
    return deck

def random_shuffle(lst):
    """ 
    (list) -> list
    Receives a list and returns a randomly ordered list containing all of the same elements.
    """
    return random.sample(lst,52)
    
def reverse(lst):
    """
    (list) -> list
    Receives a list and returns a reverse ordered list containing all of the same elements.
    """
    lst.reverse()
    return lst

print(deck())
print(random_shuffle(deck()))
print(reverse(deck()))