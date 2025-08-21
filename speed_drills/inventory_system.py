"""
Speed Drill: Inventory System Implementation
Implement an inventory management system with categories and filtering.
"""

from typing import List, Dict, Optional
from collections import defaultdict


class InventorySystem:
    """
    An inventory management system that supports:
    - Adding/removing items
    - Category-based organization
    - Price range filtering
    - Stock tracking
    """
    
    def __init__(self):
        """Initialize the inventory system."""
        # TODO: Implement storage structure
        pass
    
    def add_item(self, item_id: str, name: str, category: str, price: float, stock: int) -> bool:
        """
        Add a new item to inventory.
        
        Args:
            item_id: Unique item identifier
            name: Item name
            category: Item category
            price: Item price
            stock: Initial stock quantity
            
        Returns:
            True if item was added successfully
        """
        # TODO: Implement item addition
        pass
    
    def remove_item(self, item_id: str) -> bool:
        """
        Remove an item from inventory.
        
        Args:
            item_id: Item identifier to remove
            
        Returns:
            True if item was removed successfully
        """
        # TODO: Implement item removal
        pass
    
    def update_stock(self, item_id: str, new_stock: int) -> bool:
        """
        Update stock quantity for an item.
        
        Args:
            item_id: Item identifier
            new_stock: New stock quantity
            
        Returns:
            True if stock was updated successfully
        """
        # TODO: Implement stock update
        pass
    
    def get_items_by_category(self, category: str) -> List[Dict]:
        """
        Get all items in a specific category.
        
        Args:
            category: Category to filter by
            
        Returns:
            List of items in the category
        """
        # TODO: Implement category filtering
        pass
    
    def get_items_in_price_range(self, min_price: float, max_price: float) -> List[Dict]:
        """
        Get items within a price range.
        
        Args:
            min_price: Minimum price (inclusive)
            max_price: Maximum price (inclusive)
            
        Returns:
            List of items in the price range
        """
        # TODO: Implement price range filtering
        pass
    
    def get_low_stock_items(self, threshold: int) -> List[Dict]:
        """
        Get items with stock below threshold.
        
        Args:
            threshold: Stock threshold
            
        Returns:
            List of items below threshold
        """
        # TODO: Implement low stock filtering
        pass
    
    def get_total_value(self) -> float:
        """
        Calculate total inventory value.
        
        Returns:
            Total value of all items (price * stock)
        """
        # TODO: Implement total value calculation
        pass
    
    def search_items(self, query: str) -> List[Dict]:
        """
        Search items by name (case-insensitive).
        
        Args:
            query: Search query
            
        Returns:
            List of matching items
        """
        # TODO: Implement search functionality
        pass


# Test your implementation
if __name__ == "__main__":
    inventory = InventorySystem()
    
    # Test basic functionality
    inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
    inventory.add_item("item2", "Mouse", "Electronics", 29.99, 20)
    
    electronics = inventory.get_items_by_category("Electronics")
    print(f"Electronics items: {len(electronics)}")
    
    total_value = inventory.get_total_value()
    print(f"Total inventory value: ${total_value:.2f}")
    
    # Test search
    results = inventory.search_items("laptop")
    print(f"Search results for 'laptop': {len(results)}")
