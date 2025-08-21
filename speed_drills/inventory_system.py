"""
SPEED DRILL 4: List Operations with Filtering
Implement the Inventory class to pass all tests.
"""


from ast import Not
from collections import defaultdict


class Inventory:
    """
    An inventory system with filtering and search.
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize storage
    - add_item(self, item_id, category, price): Add inventory item
    - get_items_by_category(self, category): Filter by category
    - get_items_in_price_range(self, min_price, max_price): Filter by price
    """
    
    def __init__(self):
        """Initialize the inventory."""
        # TODO: Implement storage structure
        self.items = defaultdict(dict)
        pass
    
    def add_item(self, item_id, category, name, price, count):
        """Add an item to inventory."""
        # TODO: Implement item addition
        self.items[item_id] = {
            "item_id" : item_id,
            "name" : name,
            "category": category,
            "price": price
        }
        return True

    def remove_item(self, item_id):
        if item_id not in self.items.keys():
            return False
        else:
            del self.items[item_id]
            return True
    
    def get_items_by_category(self, category):
        """Get all items in a specific category."""
        # TODO: Implement category filtering
        pass
    
    def get_items_in_price_range(self, min_price, max_price):
        """Get items within a price range."""
        # TODO: Implement price range filtering
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    inventory = Inventory()
    print("Implement the Inventory class methods first!")
