"""
LEVEL 2: Enhanced Inventory Management
Build on Level 1 by adding filtering and search capabilities.

Time Limit: 20-25 minutes
Points: ~150 points

New Requirements (in addition to Level 1):
- Filter items by category
- Filter items by price range
- Search items by name (case-insensitive)
- Enhanced data operations
"""


class InventoryManager:
    """
    Enhanced inventory management system with filtering and search.
    
    IMPLEMENT ALL LEVEL 1 METHODS PLUS:
    - get_items_by_category(self, category): Filter by category
    - get_items_in_price_range(self, min_price, max_price): Filter by price
    - search_items_by_name(self, query): Search by name (case-insensitive)
    - get_categories(self): Get all unique categories
    - get_price_stats(self): Get min, max, average price
    """
    
    def __init__(self):
        """Initialize the inventory manager."""
        # TODO: Initialize storage for items
        pass
    
    # =================== LEVEL 1 METHODS ===================
    # Copy your Level 1 implementation here
    
    def add_item(self, item_id, name, category, price):
        """Add a new item to the inventory."""
        # TODO: Implement item addition
        pass
    
    def get_item(self, item_id):
        """Retrieve an item by its ID."""
        # TODO: Implement item retrieval
        pass
    
    def remove_item(self, item_id):
        """Remove an item from the inventory."""
        # TODO: Implement item removal
        pass
    
    def list_all_items(self):
        """Get all items in the inventory."""
        # TODO: Implement listing all items
        pass
    
    def get_item_count(self):
        """Get the total number of items in inventory."""
        # TODO: Implement item counting
        pass
    
    # =================== LEVEL 2 NEW METHODS ===================
    
    def get_items_by_category(self, category):
        """
        Get all items in a specific category.
        
        Args:
            category (str): Category to filter by
            
        Returns:
            list: List of items in the category
        """
        # TODO: Implement category filtering
        pass
    
    def get_items_in_price_range(self, min_price, max_price):
        """
        Get items within a price range (inclusive).
        
        Args:
            min_price (float): Minimum price
            max_price (float): Maximum price
            
        Returns:
            list: List of items in the price range
        """
        # TODO: Implement price range filtering
        pass
    
    def search_items_by_name(self, query):
        """
        Search items by name (case-insensitive partial match).
        
        Args:
            query (str): Search query
            
        Returns:
            list: List of items matching the query
        """
        # TODO: Implement name search
        pass
    
    def get_categories(self):
        """
        Get all unique categories in the inventory.
        
        Returns:
            list: List of unique categories
        """
        # TODO: Implement category listing
        pass
    
    def get_price_stats(self):
        """
        Get price statistics for all items.
        
        Returns:
            dict: Dictionary with 'min', 'max', 'average' keys, or None if empty
        """
        # TODO: Implement price statistics
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    inventory = InventoryManager()
    print("Level 2: Implement the enhanced InventoryManager class methods!")
