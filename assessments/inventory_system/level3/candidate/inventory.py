"""
LEVEL 3: Stock Management & Business Logic
Build on Level 2 by adding stock tracking and complex business operations.

Time Limit: 30-40 minutes
Points: ~250 points (FOCUS HERE - MOST POINTS!)

New Requirements (in addition to Level 1-2):
- Track item quantities/stock levels
- Update stock when items are sold/restocked
- Low stock alerts and notifications
- Total inventory value calculation
- Stock movement history tracking
- Business rule validation
"""


class InventoryManager:
    """
    Advanced inventory management system with stock tracking.
    
    IMPLEMENT ALL PREVIOUS LEVELS PLUS:
    - add_item(self, item_id, name, category, price, initial_stock): Now with stock
    - update_stock(self, item_id, quantity, operation): Add/remove stock
    - get_low_stock_items(self, threshold): Items below threshold
    - get_total_inventory_value(self): Total value (price * stock)
    - get_stock_history(self, item_id): Stock movement history
    - validate_sale(self, item_id, quantity): Check if sale is possible
    - process_sale(self, item_id, quantity): Execute sale and update stock
    """
    
    def __init__(self):
        """Initialize the inventory manager."""
        # TODO: Initialize storage for items, stock, and history
        pass
    
    # =================== LEVEL 1-2 METHODS ===================
    # Copy and enhance your previous implementation
    
    def add_item(self, item_id, name, category, price, initial_stock=0):
        """Add a new item with stock tracking."""
        # TODO: Enhance to include stock tracking
        pass
    
    def get_item(self, item_id):
        """Retrieve an item by its ID."""
        # TODO: Copy from Level 1
        pass
    
    def remove_item(self, item_id):
        """Remove an item from the inventory."""
        # TODO: Copy from Level 1
        pass
    
    def list_all_items(self):
        """Get all items in the inventory."""
        # TODO: Copy from Level 1
        pass
    
    def get_item_count(self):
        """Get the total number of items in inventory."""
        # TODO: Copy from Level 1
        pass
    
    def get_items_by_category(self, category):
        """Get all items in a specific category."""
        # TODO: Copy from Level 2
        pass
    
    def get_items_in_price_range(self, min_price, max_price):
        """Get items within a price range."""
        # TODO: Copy from Level 2
        pass
    
    def search_items_by_name(self, query):
        """Search items by name (case-insensitive)."""
        # TODO: Copy from Level 2
        pass
    
    def get_categories(self):
        """Get all unique categories."""
        # TODO: Copy from Level 2
        pass
    
    def get_price_stats(self):
        """Get price statistics."""
        # TODO: Copy from Level 2
        pass
    
    # =================== LEVEL 3 NEW METHODS ===================
    
    def update_stock(self, item_id, quantity, operation="add"):
        """
        Update stock for an item.
        
        Args:
            item_id (str): Item to update
            quantity (int): Quantity to add/remove
            operation (str): "add" or "remove"
            
        Returns:
            bool: True if successful, False if invalid operation
        """
        # TODO: Implement stock updates with history tracking
        pass
    
    def get_low_stock_items(self, threshold):
        """
        Get items with stock below threshold.
        
        Args:
            threshold (int): Stock level threshold
            
        Returns:
            list: Items with stock < threshold
        """
        # TODO: Implement low stock filtering
        pass
    
    def get_total_inventory_value(self):
        """
        Calculate total inventory value (price * stock for all items).
        
        Returns:
            float: Total inventory value
        """
        # TODO: Implement value calculation
        pass
    
    def get_stock_history(self, item_id):
        """
        Get stock movement history for an item.
        
        Args:
            item_id (str): Item ID
            
        Returns:
            list: List of stock movements with timestamps
        """
        # TODO: Implement history retrieval
        pass
    
    def validate_sale(self, item_id, quantity):
        """
        Check if a sale is possible (enough stock).
        
        Args:
            item_id (str): Item to sell
            quantity (int): Quantity to sell
            
        Returns:
            bool: True if sale is possible
        """
        # TODO: Implement sale validation
        pass
    
    def process_sale(self, item_id, quantity):
        """
        Process a sale (reduce stock, record transaction).
        
        Args:
            item_id (str): Item to sell
            quantity (int): Quantity to sell
            
        Returns:
            dict: Sale details if successful, None if failed
        """
        # TODO: Implement sale processing
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    inventory = InventoryManager()
    print("Level 3: Implement the stock management features!")
