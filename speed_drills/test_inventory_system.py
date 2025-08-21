"""
Test suite for InventorySystem implementation.
Run this to verify your implementation works correctly.
"""

import pytest
from inventory_system import InventorySystem


class TestInventorySystem:
    """Test cases for InventorySystem class."""
    
    def setup_method(self):
        """Set up a fresh InventorySystem instance before each test."""
        self.inventory = InventorySystem()
    
    def test_initialization(self):
        """Test that InventorySystem initializes correctly."""
        assert self.inventory is not None
    
    def test_add_item_basic(self):
        """Test basic item addition."""
        result = self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        assert result is True
    
    def test_add_item_duplicate_id(self):
        """Test adding item with duplicate ID."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        
        # Adding with same ID should work (overwrite)
        result = self.inventory.add_item("item1", "Updated Laptop", "Electronics", 1099.99, 3)
        assert result is True
    
    def test_remove_item_existing(self):
        """Test removing an existing item."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        
        result = self.inventory.remove_item("item1")
        assert result is True
    
    def test_remove_item_nonexistent(self):
        """Test removing a non-existent item."""
        result = self.inventory.remove_item("nonexistent")
        assert result is False
    
    def test_update_stock_existing(self):
        """Test updating stock for existing item."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        
        result = self.inventory.update_stock("item1", 10)
        assert result is True
    
    def test_update_stock_nonexistent(self):
        """Test updating stock for non-existent item."""
        result = self.inventory.update_stock("nonexistent", 10)
        assert result is False
    
    def test_get_items_by_category(self):
        """Test category-based filtering."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99, 20)
        self.inventory.add_item("item3", "Book", "Books", 19.99, 15)
        
        electronics = self.inventory.get_items_by_category("Electronics")
        assert len(electronics) == 2
        
        books = self.inventory.get_items_by_category("Books")
        assert len(books) == 1
        
        # Test non-existent category
        empty = self.inventory.get_items_by_category("NonExistent")
        assert len(empty) == 0
    
    def test_get_items_in_price_range(self):
        """Test price range filtering."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99, 20)
        self.inventory.add_item("item3", "Book", "Books", 19.99, 15)
        
        # Test range 0-50
        cheap_items = self.inventory.get_items_in_price_range(0, 50)
        assert len(cheap_items) == 2
        
        # Test range 100-1000
        expensive_items = self.inventory.get_items_in_price_range(100, 1000)
        assert len(expensive_items) == 1
        
        # Test single price point
        exact_price = self.inventory.get_items_in_price_range(29.99, 29.99)
        assert len(exact_price) == 1
    
    def test_get_low_stock_items(self):
        """Test low stock filtering."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99, 20)
        self.inventory.add_item("item3", "Book", "Books", 19.99, 15)
        
        # Items with stock < 10
        low_stock = self.inventory.get_low_stock_items(10)
        assert len(low_stock) == 1
        
        # Items with stock < 20
        low_stock_20 = self.inventory.get_low_stock_items(20)
        assert len(low_stock_20) == 2
    
    def test_get_total_value(self):
        """Test total inventory value calculation."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99, 20)
        
        total_value = self.inventory.get_total_value()
        expected = (999.99 * 5) + (29.99 * 20)
        assert abs(total_value - expected) < 0.01
    
    def test_search_items(self):
        """Test item search functionality."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        self.inventory.add_item("item2", "Gaming Laptop", "Electronics", 1499.99, 3)
        self.inventory.add_item("item3", "Mouse", "Electronics", 29.99, 20)
        
        # Test exact match
        laptop_results = self.inventory.search_items("Laptop")
        assert len(laptop_results) == 2
        
        # Test partial match
        gaming_results = self.inventory.search_items("Gaming")
        assert len(gaming_results) == 1
        
        # Test case insensitive
        mouse_results = self.inventory.search_items("MOUSE")
        assert len(mouse_results) == 1
        
        # Test non-existent
        empty_results = self.inventory.search_items("NonExistent")
        assert len(empty_results) == 0
    
    def test_edge_cases(self):
        """Test edge cases and error handling."""
        # Empty strings
        result = self.inventory.add_item("", "", "", 0.0, 0)
        assert result is True
        
        # Negative price and stock
        result = self.inventory.add_item("item1", "Test", "Test", -10.0, -5)
        assert result is True
        
        # Very long strings
        long_name = "x" * 1000
        long_category = "y" * 1000
        result = self.inventory.add_item("item1", long_name, long_category, 10.0, 5)
        assert result is True
    
    def test_comprehensive_workflow(self):
        """Test a complete workflow scenario."""
        # Add items
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99, 20)
        self.inventory.add_item("item3", "Book", "Books", 19.99, 15)
        
        # Update stock
        self.inventory.update_stock("item1", 3)
        
        # Remove item
        self.inventory.remove_item("item3")
        
        # Check results
        electronics = self.inventory.get_items_by_category("Electronics")
        assert len(electronics) == 2
        
        books = self.inventory.get_items_by_category("Books")
        assert len(books) == 0
        
        total_value = self.inventory.get_total_value()
        expected = (999.99 * 3) + (29.99 * 20)
        assert abs(total_value - expected) < 0.01


def run_tests():
    """Run all tests and display results."""
    print("🧪 Running InventorySystem tests...")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\nTo run tests manually, use:")
    print("python -m pytest speed_drills/test_inventory_system.py -v")


if __name__ == "__main__":
    run_tests()
