"""
CMSC 14100
Winter 2025
Homework #7

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

# CONSTANTS
JUNK_VALUE = 1
CURRENCY = "Gold"
ALL_CLASSES = {"Warrior", "Knight", "Blacksmith", "Mage"}

class Item:
    """Represents an item that can be used, crafted, or picked up."""

    def __init__(self, name, power, allowed_classes, weight, durability, value, recipe=None):
        """
        Constructor for Item.

        Args:
            name: (str): The name of the item.
            power: (int): The power of the item.
            allowed_classes: (set): The set of player classes that can use the item.
            weight: (float): The weight of the item.
            durability: (int): The durability of the item.
            value: (int): The value of the item in gold coins.
            recipe: (dictionary): The recipe for crafting the item, default is 
                                  None for an item that is not crafted
        """
        self.name = name
        self.power = power
        self.allowed_classes = allowed_classes
        self.weight = weight
        self.durability = durability
        self.value = value
        self.recipe = recipe or {}

    def use(self):
        """
        Reduces durability when used and returns whether the item is still usable.

        Args:
            None

        Returns:
            boolean, True if the item is still usable, False otherwise.
        """
        # Your Code Here
        return None

    def price(self):
        """
        Returns the current price of the item. If the item's durability is 
        0, it's value is JUNK_VALUE.

        Returns:
            int: The items actual value, or 1 if the item is broken.
        """
        # Your Code Here
        return None

    def __repr__(self):
        """
        Generates string representation of the object
        """
        return f"<{self.name} : ${self.value}>"


class Inventory:
    """Represents a player's inventory, managing items and their quantities."""

    def __init__(self):
        """
        Constructor for Inventory
        """
        # Your Code Here
        return None
    
    def add_item(self, item, quantity=1):
        """
        Adds an item to the inventory, increasing its quantity if already present.

        Args:
            item: (Item), The item to be added.
            quantity: (int), The quantity of the item to be added, default is 1.

        Returns:
            None
        """
        # Your Code Here
        return None


    def get_item(self, item_name):
        """
        Returns the item object and quantity from the inventory. Returns
        (None, None) if item is not present.

        Args:
            item_name (str): Name of the item to check
        Returns:
            tuple(Item, int): The Item object and quantity in this inventory
        """
        # Your Code Here
        return None

    def total_weight(self):
        """
        Calculates the total weight of items in the inventory.

        Returns:
            (float), The total weight of items in the inventory.
        """
        # Your Code Here
        return None
    
    def has_items(self, manifest):
        """
        Checks if the inventory contains the required items for crafting.

        Args:
            manifest: (dict), The manifest of required item names and their quantities.

        Returns:
            (boolean), True if the inventory contains the required items, False otherwise.
        """
        # Your Code Here
        return None

    def remove_items(self, manifest):
        """
        Removes required items from the inventory after crafting.

        Args:
            manifest: (dict), The manifest of item names and their quantities to remove

        Returns:
            None
        """
        # Your Code Here
        return None


class Player:
    """Represents a player with attributes such as health, XP, and inventory."""

    def __init__(self, name, player_class):
        """
        Constructor for Player class.

        Args:
            name: str, The name of the player.
            player_class: str, The class of the player.

        Returns:
            None
        """
        self.name = name
        self.player_class = player_class
        self.health = 100
        self.inventory = Inventory()

    def pick_up_item(self, item, quantity=1):
        """
        Allows the player to pick up an item if their class allows it,
        adding it to their inventory.

        Args:
            item: Item, The item to be picked up.
            quantity: int, The quantity of the item to be picked up, default is 1.

        Returns:
            bool: True if item(s) were picked up, False otherwise
        """
        # Your Code Here
        return None

    def craft_item(self, item):
        """
        Crafts an item if the player has the necessary materials in their inventory.

        Args:
            item: Item, The item to be crafted.

        Returns:
            bool: True if item was crafted, False otherwise
        """
        # Your Code Here
        return None

    def buy_item(self, item_name, quantity, other_player):
        """
        Allows the player to buy an item from another player in exchange for gold.
        
        Inputs:
            item_name (str): Name of the item to be bought
            quantity (int): Quantity to be bought
            other_player (Player): Player to buy from

        Outputs:
            (bool): True if sale is successful, False if not
        """
        # Your Code Here
        return None

    def sell_item(self, item_name, quantity, other_player):
        """
        Allows the player to sell an item to a player for gold.
        
        Inputs:
            item_name (str): Name of the item to be sold
            quantity (int): Quantity to be sold
            other_player (Player): Player to sell to

        Outputs:
            (bool): True if sale is successful, False if not
        """
        # Your Code Here
        return None

    def __repr__(self):
        """
        Representation of the player.

        Args:
            None

        Returns:
            string, The name of the player.
        """
        return self.name
