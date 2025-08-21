"""
Unit Tests for Level 4: Advanced Operations & Data Management
"""

import pytest
import sys
import os
import time

# Add the candidate directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'candidate'))

from inventory import InventoryManager


class TestInventoryManagerLevel4:
    """Test cases for Level 4 InventoryManager."""
    
    def setup_method(self):
        """Set up a fresh InventoryManager instance before each test."""
        self.inventory = InventoryManager()
    
    def test_initialization(self):
        """Test that InventoryManager initializes correctly."""
        assert self.inventory is not None
        assert hasattr(self.inventory, 'items')
        assert hasattr(self.inventory, 'stock_history')
        assert hasattr(self.inventory, 'backups')
    
    # =================== LEVEL 1-3 FUNCTIONALITY TESTS ===================
    
    def test_all_previous_levels_work(self):
        """Test that all previous level functionality still works."""
        # Level 1: Basic CRUD
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        assert self.inventory.get_item_count() == 1
        
        # Level 2: Filtering
        electronics = self.inventory.get_items_by_category("Electronics")
        assert len(electronics) == 1
        
        # Level 3: Stock management
        self.inventory.update_stock("item1", 5, "add")
        assert self.inventory.get_item("item1")['stock'] == 15
        
        sale = self.inventory.process_sale("item1", 3)
        assert sale['remaining_stock'] == 12
    
    # =================== LEVEL 4 NEW TESTS ===================
    
    def test_backup_inventory(self):
        """Test inventory backup creation."""
        # Add some data
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99, 20)
        
        result = self.inventory.backup_inventory("backup1")
        assert result is True
        assert "backup1" in self.inventory.backups
    
    def test_restore_inventory_existing(self):
        """Test restoring from existing backup."""
        # Create initial state
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        self.inventory.backup_inventory("backup1")
        
        # Modify state
        self.inventory.add_item("item2", "Mouse", "Electronics", 29.99, 20)
        self.inventory.update_stock("item1", 5, "remove")
        
        # Restore
        result = self.inventory.restore_inventory("backup1")
        assert result is True
        
        # Should be back to original state
        assert self.inventory.get_item_count() == 1
        assert self.inventory.get_item("item1")['stock'] == 10
        assert self.inventory.get_item("item2") is None
    
    def test_restore_inventory_nonexistent(self):
        """Test restoring from non-existent backup."""
        result = self.inventory.restore_inventory("nonexistent")
        assert result is False
    
    def test_bulk_add_items_success(self):
        """Test successful bulk item addition."""
        items_to_add = [
            {'id': 'bulk1', 'name': 'Item 1', 'category': 'Test', 'price': 10.0, 'stock': 5},
            {'id': 'bulk2', 'name': 'Item 2', 'category': 'Test', 'price': 20.0, 'stock': 10},
            {'id': 'bulk3', 'name': 'Item 3', 'category': 'Test', 'price': 30.0}  # No stock specified
        ]
        
        result = self.inventory.bulk_add_items(items_to_add)
        
        assert result['added'] == 3
        assert len(result['failed']) == 0
        assert self.inventory.get_item_count() == 3
        
        # Check items were added correctly
        item1 = self.inventory.get_item('bulk1')
        assert item1['stock'] == 5
        
        item3 = self.inventory.get_item('bulk3')
        assert item3['stock'] == 0  # Default stock
    
    def test_bulk_add_items_with_failures(self):
        """Test bulk addition with some failures."""
        # Add an item first to create duplicate
        self.inventory.add_item("existing", "Existing Item", "Test", 50.0, 5)
        
        items_to_add = [
            {'id': 'new1', 'name': 'New Item', 'category': 'Test', 'price': 10.0},
            {'id': 'existing', 'name': 'Duplicate', 'category': 'Test', 'price': 20.0},  # Should fail
            {'invalid': 'data'},  # Missing required fields
        ]
        
        result = self.inventory.bulk_add_items(items_to_add)
        
        assert result['added'] == 1  # Only new1 should succeed
        assert len(result['failed']) == 2
        assert 'existing' in result['failed']
    
    def test_bulk_update_stock_success(self):
        """Test successful bulk stock updates."""
        # Add items first
        self.inventory.add_item("item1", "Item 1", "Test", 10.0, 20)
        self.inventory.add_item("item2", "Item 2", "Test", 20.0, 30)
        
        updates = [
            {'item_id': 'item1', 'quantity': 10, 'operation': 'add'},
            {'item_id': 'item2', 'quantity': 5, 'operation': 'remove'}
        ]
        
        result = self.inventory.bulk_update_stock(updates)
        
        assert result['updated'] == 2
        assert len(result['failed']) == 0
        
        assert self.inventory.get_item('item1')['stock'] == 30
        assert self.inventory.get_item('item2')['stock'] == 25
    
    def test_bulk_update_stock_with_failures(self):
        """Test bulk stock updates with some failures."""
        self.inventory.add_item("item1", "Item 1", "Test", 10.0, 5)
        
        updates = [
            {'item_id': 'item1', 'quantity': 3, 'operation': 'add'},  # Should work
            {'item_id': 'item1', 'quantity': 10, 'operation': 'remove'},  # Should fail - not enough stock
            {'item_id': 'nonexistent', 'quantity': 5, 'operation': 'add'},  # Should fail - no item
        ]
        
        result = self.inventory.bulk_update_stock(updates)
        
        assert result['updated'] == 1  # Only first update should succeed
        assert len(result['failed']) == 2
        assert 'nonexistent' in result['failed']
        
        # Stock should be 8 (5 + 3)
        assert self.inventory.get_item('item1')['stock'] == 8
    
    def test_export_inventory(self):
        """Test inventory export functionality."""
        # Add some data
        self.inventory.add_item("item1", "Laptop", "Electronics", 999.99, 10)
        self.inventory.update_stock("item1", 5, "add")
        
        exported_data = self.inventory.export_inventory()
        
        assert 'items' in exported_data
        assert 'stock_history' in exported_data
        assert 'export_timestamp' in exported_data
        assert 'version' in exported_data
        
        assert len(exported_data['items']) == 1
        assert 'item1' in exported_data['items']
        assert exported_data['items']['item1']['stock'] == 15
    
    def test_import_inventory_valid_data(self):
        """Test importing valid inventory data."""
        # Create test data
        test_data = {
            'items': {
                'item1': {'id': 'item1', 'name': 'Test Item', 'category': 'Test', 'price': 50.0, 'stock': 10}
            },
            'stock_history': {
                'item1': [{'timestamp': time.time(), 'operation': 'initial', 'quantity': 10, 'new_stock': 10}]
            },
            'version': '1.0'
        }
        
        result = self.inventory.import_inventory(test_data)
        assert result is True
        
        # Verify data was imported
        assert self.inventory.get_item_count() == 1
        item = self.inventory.get_item('item1')
        assert item['name'] == 'Test Item'
        assert item['stock'] == 10
        
        history = self.inventory.get_stock_history('item1')
        assert len(history) >= 1
    
    def test_import_inventory_invalid_data(self):
        """Test importing invalid data."""
        # Missing required fields
        invalid_data = {
            'items': {
                'item1': {'id': 'item1', 'name': 'Test'}  # Missing category, price, stock
            }
        }
        
        result = self.inventory.import_inventory(invalid_data)
        assert result is False
        
        # No data should be imported
        assert self.inventory.get_item_count() == 0
    
    def test_import_inventory_missing_items_key(self):
        """Test importing data without items key."""
        invalid_data = {'stock_history': {}}
        
        result = self.inventory.import_inventory(invalid_data)
        assert result is False
    
    def test_get_system_stats_with_data(self):
        """Test system statistics with data."""
        # Add diverse data
        self.inventory.add_item("laptop1", "MacBook", "Electronics", 2000.0, 5)
        self.inventory.add_item("laptop2", "Dell Laptop", "Electronics", 1000.0, 10)
        self.inventory.add_item("mouse1", "Mouse", "Electronics", 50.0, 100)
        self.inventory.add_item("book1", "Python Book", "Books", 40.0, 3)
        
        stats = self.inventory.get_system_stats()
        
        assert stats['total_items'] == 4
        assert stats['total_categories'] == 2
        assert stats['total_stock_units'] == 118
        assert stats['total_inventory_value'] == (2000*5 + 1000*10 + 50*100 + 40*3)
        assert stats['low_stock_items'] == 2  # laptop1 and book1 have < 10 stock
        assert stats['average_stock_per_item'] == 118/4
        assert set(stats['categories']) == {'Electronics', 'Books'}
    
    def test_get_system_stats_empty(self):
        """Test system statistics when empty."""
        stats = self.inventory.get_system_stats()
        
        assert stats['total_items'] == 0
        assert stats['total_categories'] == 0
        assert stats['total_stock_units'] == 0
        assert stats['total_inventory_value'] == 0.0
        assert stats['low_stock_items'] == 0
    
    def test_comprehensive_level4_workflow(self):
        """Test complete Level 4 workflow."""
        # Initial setup
        initial_items = [
            {'id': 'laptop1', 'name': 'MacBook Pro', 'category': 'Electronics', 'price': 2499.99, 'stock': 20},
            {'id': 'mouse1', 'name': 'Wireless Mouse', 'category': 'Electronics', 'price': 79.99, 'stock': 100},
            {'id': 'book1', 'name': 'Python Guide', 'category': 'Books', 'price': 39.99, 'stock': 50}
        ]
        
        # Bulk add
        bulk_result = self.inventory.bulk_add_items(initial_items)
        assert bulk_result['added'] == 3
        
        # Create backup
        self.inventory.backup_inventory("initial_state")
        
        # Make changes
        stock_updates = [
            {'item_id': 'laptop1', 'quantity': 10, 'operation': 'remove'},
            {'item_id': 'mouse1', 'quantity': 50, 'operation': 'add'}
        ]
        update_result = self.inventory.bulk_update_stock(stock_updates)
        assert update_result['updated'] == 2
        
        # Process some sales
        sale1 = self.inventory.process_sale("laptop1", 5)
        sale2 = self.inventory.process_sale("book1", 10)
        
        assert sale1 is not None
        assert sale2 is not None
        
        # Export current state
        exported = self.inventory.export_inventory()
        assert len(exported['items']) == 3
        
        # Restore to backup
        restored = self.inventory.restore_inventory("initial_state")
        assert restored is True
        
        # Should be back to original state
        assert self.inventory.get_item("laptop1")['stock'] == 20
        assert self.inventory.get_item("mouse1")['stock'] == 100
        assert self.inventory.get_item("book1")['stock'] == 50
        
        # Get final stats
        stats = self.inventory.get_system_stats()
        assert stats['total_items'] == 3
        assert stats['total_backups'] == 1


def run_tests():
    """Run all tests and display results."""
    print("🧪 Level 4: Advanced Operations & Data Management")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ Level 4 tests completed!")
    print("\nTo run tests manually, use:")
    print("python -m pytest assessments/inventory_system/level4/tests/test_inventory.py -v")


if __name__ == "__main__":
    run_tests()
