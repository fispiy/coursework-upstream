"""
CMSC 14100
Winter 2025
Homework #6

We will be using anonymous grading, so please do NOT include your name
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

#############################################################################
#                                                                           #
# Important note: some of the tasks in this assignment have task-specific   #
# requirements/restrictions concerning the language constructs that you are #
# allowed to use in your solution. See the assignment writeup for details.  #
#                                                                           #
#############################################################################


# Constants
PLAYER_CLASSES = {"KNIGHT", "MAGE", "THIEF"}
LEVEL_LIMITS = [10,20,35,50,100,150, 200, 250, 500]

# Exercise 1
def validate_recipe(recipe):
    """
    Check if the given crafting recipe is valid. A crafting recipe is valid if
    it has a positive integer level, a valid player class, either: one 
    material with more than one quantity or two different materials with at 
    least one quantity each, and a positive integer power.

    Input:
        recipe (dict[str,Any]): a recipe dict

    Output (bool): True if recipe is valid, False if not.
    """
    return None 


# Exercise 2.
def can_craft(recipe, player):
    """
    Check if the given player has the required level and class to craft the
    given recipe.

    Input:
        recipe (dict[str,Any]): a recipe dict
        player (dict[str,Any]): a player dict

    Output (bool): True if recipe is craftable by the player, False if not.
    """
    return None


# Exercise 3.
def filter_level_class(recipes, player):
    """
    Given a list of recipes, produce a list of recipes that are valid for the
    given player (i.e. the player has the required class and level). Does not 
    check if the player has the materials to craft the recipe.

    Input:
        recipe (list[dict[str,Any]]): a list of recipe dicts
        player (dict[str,Any]): a player dict
    Output (list[dict[str,Any]]): a list of recipes that the player can craft
        based solely on their level and class
    """
    return None


# Exercise 4.
def filter_recipe_materials(recipes, materials_set):
    """
    Given a set of materials, produce a list that contains only those recipes 
    that require only the materials in the given set.

    Input:
        recipe (list[dict[str,Any]]): a list of recipe dicts
        materials (set[str]): a set of materials

    Output (list[dict[str,Any]]): a list of recipes that the player can craft
        based on the materials in the set
    """
    return None


# Exercise 5.
def calculate_inventory_weight(player):
    """
    Given an inventory dict, compute the weight of all items in the inventory 
    and add it to the player dict. The weight of every item is 1.0

    Input:
        player (dict[str, Any]): a player dict

    Output: None
    """
    return None


# Exercise 6.
def add_items_to_inventory(player, items):
    """
    Given a player and a list of items, add the given items to the player's 
    inventory as long as the limit for the player's class is not reached and
    return the number of items that were added.

    Input 
        player (dict[str, Any]): a player dict
        items (list[str]): a list of items to add to the inventory

    Output (int): the number of items added to the inventory
    """
    return None


# Exercise 7.
def all_craftable_items(recipes, player):
    """
    Given a list of recipes and a player dictionary, produce a list of all 
    recipes that the given player is able to craft with their current level,
    class, and materials on hand.

    Input:
        recipes (list[dict[str,Any]]): list of recipe dictionaries
        player (dict[str,Any]): player dictionary

    Output (list[dict[str,Any]]): a list of recipes that the player can craft
        with their level, class, and materials
    """
    return None


# Exercise 8.
def craft_max_power(recipes, player):
    """
    Given a list of recipes and a player dictionary, craft an item with the 
    greatest power from the given list of recipes that the player is able to
    craft given their class, level, and materials in their inventory.

    If successful, the materials in the inventory should be consumed and the 
    crafted item should be placed in the player's inventory. The power of the
    crafted item should be produced as output.

    Input:
        recipes (list[dict[str,Any]]): list of recipe dictionaries
        player (dict[str,Any]): player dictionary

    Output (int): The power of the crafted item if successful, and 0 otherwise
    """
    return None
