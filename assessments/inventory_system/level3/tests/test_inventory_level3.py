"""
Unit Tests for Level 3: Stock Management & Business Logic
"""

import pytest
import sys
import os
import time

# Add the candidate directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'candidate'))

from inventory import InventoryManager


class TestInventoryManagerLevel3:
    """Test cases for Level 3 InventoryManager."""
    
    def setup_method(self):
        """Set up a fresh InventoryManager instance before each test."""
        self.inventory = InventoryManager()
    
    def test_initialization(self):
        """Test that InventoryManager initializes correctly."""
        assert self.inventory is not None
        assert self.inventory.get_item_count() == 0
    
    # =================== LEVEL 1-2 TESTS ===================
    
    def test_add_item_with_stock(self):
        """Test adding item with initial stock."""
        result = self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        assert result is True
        
        item = self.inventory.get_item("item1")
        assert item['stock'] == 10
    
    def test_level2_filtering_still_works(self):
        """Test that Level 2 filtering still works with stock."""
        self.inventory.add_item("laptop1", "MacBook", "Electronics", 2499.99, 5)
        self.inventory.add_item("mouse1", "Mouse", "Electronics", 79.99, 20)
        self.inventory.add_item("book1", "Python", "Books", 39.99, 15)
        
        electronics = self.inventory.get_items_by_category("Electronics")
        assert len(electronics) == 2
        
        expensive = self.inventory.get_items_in_price_range(1000, 3000)
        assert len(expensive) == 1
        
        search_results = self.inventory.search_items_by_name("python")
        assert len(search_results) == 1
    
    # =================== LEVEL 3 NEW TESTS ===================
    
    def test_update_stock_add(self):
        """Test adding stock to an item."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        
        result = self.inventory.update_stock("item1", 5, "add")
        assert result is True
        
        item = self.inventory.get_item("item1")
        assert item['stock'] == 15
    
    def test_update_stock_remove_valid(self):
        """Test removing stock when sufficient quantity available."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        
        result = self.inventory.update_stock("item1", 3, "remove")
        assert result is True
        
        item = self.inventory.get_item("item1")
        assert item['stock'] == 7
    
    def test_update_stock_remove_insufficient(self):
        """Test removing more stock than available."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        
        result = self.inventory.update_stock("item1", 10, "remove")
        assert result is False
        
        # Stock should remain unchanged
        item = self.inventory.get_item("item1")
        assert item['stock'] == 5
    
    def test_update_stock_nonexistent_item(self):
        """Test updating stock for non-existent item."""
        result = self.inventory.update_stock("nonexistent", 5, "add")
        assert result is False
    
    def test_update_stock_invalid_operation(self):
        """Test invalid stock operation."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        
        result = self.inventory.update_stock("item1", 5, "invalid")
        assert result is False
    
    def test_get_low_stock_items(self):
        """Test low stock filtering."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99, 20)
        self.inventory.add_item("item3", "Book", "Books", 19.99, 2)
        
        # Items with stock < 10
        low_stock = self.inventory.get_low_stock_items(10)
        assert len(low_stock) == 2
        
        # Items with stock < 5
        very_low_stock = self.inventory.get_low_stock_items(5)
        assert len(very_low_stock) == 1
        
        # Items with stock < 1
        no_stock = self.inventory.get_low_stock_items(1)
        assert len(no_stock) == 0
    
    def test_get_total_inventory_value(self):
        """Test total inventory value calculation."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 1000.00, 5)
        self.inventory.add_item("item2", "Mouse", "Electronics", 50.00, 10)
        
        total_value = self.inventory.get_total_inventory_value()
        expected = (1000.00 * 5) + (50.00 * 10)
        assert abs(total_value - expected) < 0.01
    
    def test_get_total_inventory_value_empty(self):
        """Test total value when inventory is empty."""
        total_value = self.inventory.get_total_inventory_value()
        assert total_value == 0.0
    
    def test_get_stock_history(self):
        """Test stock history tracking."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        
        # Initial history should exist
        history = self.inventory.get_stock_history("item1")
        assert len(history) >= 1
        assert history[0]['operation'] == 'initial'
        assert history[0]['quantity'] == 10
        
        # Add more stock
        self.inventory.update_stock("item1", 5, "add")
        history = self.inventory.get_stock_history("item1")
        assert len(history) >= 2
        assert history[-1]['operation'] == 'add'
        assert history[-1]['quantity'] == 5
    
    def test_get_stock_history_nonexistent(self):
        """Test stock history for non-existent item."""
        history = self.inventory.get_stock_history("nonexistent")
        assert history == []
    
    def test_validate_sale_sufficient_stock(self):
        """Test sale validation with sufficient stock."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        
        assert self.inventory.validate_sale("item1", 5) is True
        assert self.inventory.validate_sale("item1", 10) is True
    
    def test_validate_sale_insufficient_stock(self):
        """Test sale validation with insufficient stock."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 5)
        
        assert self.inventory.validate_sale("item1", 10) is False
    
    def test_validate_sale_nonexistent_item(self):
        """Test sale validation for non-existent item."""
        assert self.inventory.validate_sale("nonexistent", 1) is False
    
    def test_process_sale_successful(self):
        """Test successful sale processing."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 1000.00, 10)
        
        sale = self.inventory.process_sale("item1", 3)
        
        assert sale is not None
        assert sale['item_id'] == "item1"
        assert sale['item_name'] == "Laptop"
        assert sale['quantity_sold'] == 3
        assert sale['unit_price'] == 1000.00
        assert sale['total_amount'] == 3000.00
        assert sale['remaining_stock'] == 7
        
        # Verify stock was actually updated
        item = self.inventory.get_item("item1")
        assert item['stock'] == 7
    
    def test_process_sale_insufficient_stock(self):
        """Test sale processing with insufficient stock."""
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 3)
        
        sale = self.inventory.process_sale("item1", 5)
        assert sale is None
        
        # Stock should remain unchanged
        item = self.inventory.get_item("item1")
        assert item['stock'] == 3
    
    def test_process_sale_nonexistent_item(self):
        """Test sale processing for non-existent item."""
        sale = self.inventory.process_sale("nonexistent", 1)
        assert sale is None
    
    def test_comprehensive_stock_workflow(self):
        """Test complete stock management workflow."""
        # Add items with stock
        self.inventory.add_item("laptop1", "MacBook Pro", "Electronics", 2499.99, 20)
        self.inventory.add_item("mouse1", "Wireless Mouse", "Electronics", 79.99, 100)
        
        # Restock
        self.inventory.update_stock("laptop1", 10, "add")
        assert self.inventory.get_item("laptop1")['stock'] == 30
        
        # Process sales
        sale1 = self.inventory.process_sale("laptop1", 5)
        assert sale1['remaining_stock'] == 25
        
        sale2 = self.inventory.process_sale("mouse1", 20)
        assert sale2['remaining_stock'] == 80
        
        # Check low stock
        low_stock = self.inventory.get_low_stock_items(30)
        assert len(low_stock) == 1  # Only laptop should be below 30
        
        # Check total value
        total_value = self.inventory.get_total_inventory_value()
        expected = (2499.99 * 25) + (79.99 * 80)
        assert abs(total_value - expected) < 0.01
        
        # Check history
        laptop_history = self.inventory.get_stock_history("laptop1")
        assert len(laptop_history) >= 3  # initial, add, sale
        
        mouse_history = self.inventory.get_stock_history("mouse1")
        assert len(mouse_history) >= 2  # initial, sale
    
    def test_edge_cases_level3(self):
        """Test edge cases for Level 3 functionality."""
        # Zero stock item
        self.inventory.add_item("item1", "Test", "Test", 10.0, 0)
        
        # Can't sell zero stock
        assert self.inventory.validate_sale("item1", 1) is False
        assert self.inventory.process_sale("item1", 1) is None
        
        # Can add to zero stock
        assert self.inventory.update_stock("item1", 5, "add") is True
        assert self.inventory.get_item("item1")['stock'] == 5
        
        # Can't remove from zero stock
        self.inventory.update_stock("item1", 5, "remove")  # Back to 0
        assert self.inventory.update_stock("item1", 1, "remove") is False


def run_tests():
    """Run all tests and display results."""
    print("🧪 Level 3: Stock Management & Business Logic")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ Level 3 tests completed!")
    print("\nTo run tests manually, use:")
    print("python -m pytest assessments/inventory_system/level3/tests/test_inventory.py -v")


if __name__ == "__main__":
    run_tests()
