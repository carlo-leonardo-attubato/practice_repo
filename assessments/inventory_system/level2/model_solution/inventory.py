"""
LEVEL 2: Enhanced Inventory Features - MODEL SOLUTION
Category management, search functionality, alerts, and supplier management.
"""

import time
from collections import defaultdict


class InventorySystem:
    """Enhanced inventory system with categories and search."""
    
    def __init__(self):
        """Initialize the enhanced inventory system."""
        self.items = {}  # item_name -> item_data
        self.categories = set()  # Set of category names
        self.suppliers = {}  # supplier_id -> supplier_data
        self.low_stock_thresholds = {}  # item_name -> threshold
        self.next_supplier_id = 1001
    
    def add_category(self, category_name):
        """Add a new category."""
        self.categories.add(category_name)
        return True
    
    def add_item(self, name, price, category, quantity, supplier_id=None):
        """Add a new item to inventory."""
        if name in self.items:
            return False
        
        self.items[name] = {
            'name': name,
            'price': price,
            'category': category,
            'quantity': quantity,
            'supplier_id': supplier_id,
            'created_at': time.time()
        }
        
        # Add category if it doesn't exist
        self.categories.add(category)
        
        return True
    
    def get_item(self, name):
        """Get item information."""
        return self.items.get(name)
    
    def update_quantity(self, name, new_quantity):
        """Update item quantity."""
        if name in self.items:
            self.items[name]['quantity'] = new_quantity
            return True
        return False
    
    def get_items_by_category(self, category):
        """Get all items in a specific category."""
        return [item for item in self.items.values() if item['category'] == category]
    
    def search_items(self, query, exact=False):
        """Search for items by name."""
        if exact:
            return [item for item in self.items.values() if item['name'] == query]
        else:
            return [item for item in self.items.values() if query.lower() in item['name'].lower()]
    
    def set_low_stock_threshold(self, item_name, threshold):
        """Set low stock threshold for an item."""
        self.low_stock_thresholds[item_name] = threshold
    
    def get_low_stock_alerts(self):
        """Get items that are below their low stock threshold."""
        alerts = []
        for item_name, threshold in self.low_stock_thresholds.items():
            if item_name in self.items:
                item = self.items[item_name]
                if item['quantity'] <= threshold:
                    alerts.append({
                        'name': item_name,
                        'current_quantity': item['quantity'],
                        'threshold': threshold
                    })
        return alerts
    
    def add_supplier(self, name, email):
        """Add a new supplier."""
        supplier_id = str(self.next_supplier_id)
        self.next_supplier_id += 1
        
        self.suppliers[supplier_id] = {
            'id': supplier_id,
            'name': name,
            'email': email,
            'created_at': time.time()
        }
        
        return supplier_id
    
    def get_supplier_info(self, supplier_id):
        """Get supplier information."""
        return self.suppliers.get(supplier_id)
    
    def get_all_items(self):
        """Get all items in inventory."""
        return list(self.items.values())
    
    def get_total_value(self):
        """Calculate total inventory value."""
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total


if __name__ == "__main__":
    inventory = InventorySystem()
    
    # Test the implementation
    print("Testing Level 2 functionality...")
    
    # Add items
    inventory.add_item("laptop1", "MacBook Pro", "Electronics", 2499.99)
    inventory.add_item("laptop2", "Dell Laptop", "Electronics", 1299.99)
    inventory.add_item("mouse1", "Wireless Mouse", "Electronics", 79.99)
    inventory.add_item("book1", "Python Programming", "Books", 39.99)
    inventory.add_item("book2", "Data Structures", "Books", 49.99)
    
    # Test category filtering
    electronics = inventory.get_items_by_category("Electronics")
    print(f"Electronics items: {len(electronics)}")
    
    books = inventory.get_items_by_category("Books")
    print(f"Books: {len(books)}")
    
    # Test price filtering
    expensive_items = inventory.get_items_in_price_range(1000, 3000)
    print(f"Items $1000-$3000: {len(expensive_items)}")
    
    cheap_items = inventory.get_items_in_price_range(0, 100)
    print(f"Items under $100: {len(cheap_items)}")
    
    # Test search
    laptop_results = inventory.search_items_by_name("laptop")
    print(f"Items with 'laptop' in name: {len(laptop_results)}")
    
    programming_results = inventory.search_items_by_name("Programming")
    print(f"Items with 'Programming' in name: {len(programming_results)}")
    
    # Test categories
    categories = inventory.get_categories()
    print(f"Categories: {categories}")
    
    # Test price stats
    stats = inventory.get_price_stats()
    print(f"Price stats: min=${stats['min']:.2f}, max=${stats['max']:.2f}, avg=${stats['average']:.2f}")
    
    print("✅ Level 2 implementation complete!")
