"""
LEVEL 1: Basic Inventory Management
Implement basic CRUD operations for inventory items.

Time Limit: 15-20 minutes
Points: ~100 points

Requirements:
- Add items with ID, name, category, price
- Retrieve items by ID
- List all items
- Remove items by ID
"""


class InventoryManager:
    """
    Basic inventory management system.
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize the inventory
    - add_item(self, item_id, name, category, price): Add a new item
    - get_item(self, item_id): Get item by ID
    - remove_item(self, item_id): Remove item by ID
    - list_all_items(self): Get all items
    - get_item_count(self): Get total number of items
    """
    
    def __init__(self):
        """Initialize the inventory manager."""
        # TODO: Initialize storage for items
        pass
    
    def add_item(self, item_id, name, category, price):
        """
        Add a new item to the inventory.
        
        Args:
            item_id (str): Unique identifier for the item
            name (str): Item name
            category (str): Item category
            price (float): Item price
            
        Returns:
            bool: True if added successfully, False if item_id already exists
        """
        # TODO: Implement item addition
        pass
    
    def get_item(self, item_id):
        """
        Retrieve an item by its ID.
        
        Args:
            item_id (str): The item ID to retrieve
            
        Returns:
            dict: Item data if found, None if not found
        """
        # TODO: Implement item retrieval
        pass
    
    def remove_item(self, item_id):
        """
        Remove an item from the inventory.
        
        Args:
            item_id (str): The item ID to remove
            
        Returns:
            bool: True if removed successfully, False if item not found
        """
        # TODO: Implement item removal
        pass
    
    def list_all_items(self):
        """
        Get all items in the inventory.
        
        Returns:
            list: List of all items
        """
        # TODO: Implement listing all items
        pass
    
    def get_item_count(self):
        """
        Get the total number of items in inventory.
        
        Returns:
            int: Number of items
        """
        # TODO: Implement item counting
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    inventory = InventoryManager()
    print("Level 1: Implement the InventoryManager class methods!")
