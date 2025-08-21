"""
Unit Tests for Level 1: Basic Inventory Management
"""

import pytest
import sys
import os

# Add the candidate directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'candidate'))

from inventory import InventoryManager


class TestInventoryManagerLevel1:
    """Test cases for Level 1 InventoryManager."""
    
    def setup_method(self):
        """Set up a fresh InventoryManager instance before each test."""
        self.inventory = InventoryManager()
    
    def test_initialization(self):
        """Test that InventoryManager initializes correctly."""
        assert self.inventory is not None
        assert self.inventory.get_item_count() == 0
    
    def test_add_item_basic(self):
        """Test basic item addition."""
        result = self.inventory.add_item("item1", "Laptop", "Electronics", 999.99)
        assert result is True
        assert self.inventory.get_item_count() == 1
    
    def test_add_item_duplicate(self):
        """Test adding item with duplicate ID."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99)
        result = self.inventory.add_item("item1", "Different Laptop", "Electronics", 1299.99)
        assert result is False
        assert self.inventory.get_item_count() == 1
    
    def test_get_item_existing(self):
        """Test retrieving an existing item."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99)
        item = self.inventory.get_item("item1")
        
        assert item is not None
        assert item['id'] == "item1"
        assert item['name'] == "Laptop"
        assert item['category'] == "Electronics"
        assert item['price'] == 999.99
    
    def test_get_item_nonexistent(self):
        """Test retrieving a non-existent item."""
        item = self.inventory.get_item("nonexistent")
        assert item is None
    
    def test_remove_item_existing(self):
        """Test removing an existing item."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99)
        result = self.inventory.remove_item("item1")
        
        assert result is True
        assert self.inventory.get_item_count() == 0
        assert self.inventory.get_item("item1") is None
    
    def test_remove_item_nonexistent(self):
        """Test removing a non-existent item."""
        result = self.inventory.remove_item("nonexistent")
        assert result is False
    
    def test_list_all_items_empty(self):
        """Test listing items when inventory is empty."""
        items = self.inventory.list_all_items()
        assert items == []
    
    def test_list_all_items_with_data(self):
        """Test listing items with data."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99)
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99)
        
        items = self.inventory.list_all_items()
        assert len(items) == 2
        
        # Check that both items are in the list
        item_ids = [item['id'] for item in items]
        assert "item1" in item_ids
        assert "item2" in item_ids
    
    def test_get_item_count(self):
        """Test item count functionality."""
        assert self.inventory.get_item_count() == 0
        
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99)
        assert self.inventory.get_item_count() == 1
        
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99)
        assert self.inventory.get_item_count() == 2
        
        self.inventory.remove_item("item1")
        assert self.inventory.get_item_count() == 1
    
    def test_comprehensive_workflow(self):
        """Test a complete workflow."""
        # Add multiple items
        self.inventory.add_item("laptop1", "MacBook Pro", "Electronics", 2499.99)
        self.inventory.add_item("mouse1", "Wireless Mouse", "Electronics", 79.99)
        self.inventory.add_item("book1", "Python Guide", "Books", 39.99)
        
        # Verify count
        assert self.inventory.get_item_count() == 3
        
        # Verify retrieval
        laptop = self.inventory.get_item("laptop1")
        assert laptop['name'] == "MacBook Pro"
        assert laptop['price'] == 2499.99
        
        # Verify listing
        all_items = self.inventory.list_all_items()
        assert len(all_items) == 3
        
        # Remove an item
        removed = self.inventory.remove_item("mouse1")
        assert removed is True
        assert self.inventory.get_item_count() == 2
        
        # Verify it's gone
        assert self.inventory.get_item("mouse1") is None
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Empty strings
        result = self.inventory.add_item("", "Empty ID", "Test", 0.0)
        assert result is True
        
        # Zero price
        result = self.inventory.add_item("free_item", "Free Item", "Test", 0.0)
        assert result is True
        
        # Negative price
        result = self.inventory.add_item("negative", "Negative Price", "Test", -10.0)
        assert result is True


def run_tests():
    """Run all tests and display results."""
    print("🧪 Level 1: Basic Inventory Management")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ Level 1 tests completed!")
    print("\nTo run tests manually, use:")
    print("python -m pytest assessments/inventory_system/level1/tests/test_inventory.py -v")


if __name__ == "__main__":
    run_tests()
