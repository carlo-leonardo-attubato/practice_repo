import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from inventory_system.level2.model_solution.inventory import InventorySystem

class TestInventoryLevel2:
    def test_category_management(self):
        inventory = InventorySystem()
        
        # Add categories
        inventory.add_category("electronics")
        inventory.add_category("clothing")
        
        # Add items to categories
        inventory.add_item("laptop", 999.99, "electronics", 10)
        inventory.add_item("shirt", 29.99, "clothing", 50)
        
        # Test category filtering
        electronics = inventory.get_items_by_category("electronics")
        assert len(electronics) == 1
        assert electronics[0]["name"] == "laptop"
        
    def test_search_functionality(self):
        inventory = InventorySystem()
        
        # Add items
        inventory.add_item("laptop", 999.99, "electronics", 10)
        inventory.add_item("laptop charger", 49.99, "electronics", 20)
        inventory.add_item("laptop stand", 29.99, "accessories", 15)
        
        # Test search
        results = inventory.search_items("laptop")
        assert len(results) == 3
        
        # Test exact search
        exact_results = inventory.search_items("laptop", exact=True)
        assert len(exact_results) == 1
        
    def test_inventory_alerts(self):
        inventory = InventorySystem()
        
        # Set low stock threshold
        inventory.set_low_stock_threshold("laptop", 5)
        
        # Add item with low stock
        inventory.add_item("laptop", 999.99, "electronics", 3)
        
        # Test low stock alerts
        alerts = inventory.get_low_stock_alerts()
        assert len(alerts) == 1
        assert alerts[0]["name"] == "laptop"
        
    def test_supplier_management(self):
        inventory = InventorySystem()
        
        # Add supplier
        supplier_id = inventory.add_supplier("TechCorp", "tech@corp.com")
        assert supplier_id is not None
        
        # Add item with supplier
        inventory.add_item("laptop", 999.99, "electronics", 10, supplier_id=supplier_id)
        
        # Test supplier info
        supplier_info = inventory.get_supplier_info(supplier_id)
        assert supplier_info["name"] == "TechCorp"
