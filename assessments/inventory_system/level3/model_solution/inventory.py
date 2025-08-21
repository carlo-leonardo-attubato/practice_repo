"""
LEVEL 3: Stock Management & Business Logic - MODEL SOLUTION
Advanced inventory with stock tracking and business operations.
"""

import time


class InventoryManager:
    """Advanced inventory management system with stock tracking."""
    
    def __init__(self):
        """Initialize the inventory manager."""
        self.items = {}  # item_id -> item_data
        self.stock_history = {}  # item_id -> list of movements
    
    # =================== LEVEL 1-2 METHODS ===================
    
    def add_item(self, item_id, name, category, price, initial_stock=0):
        """Add a new item with stock tracking."""
        if item_id in self.items:
            return False
        
        self.items[item_id] = {
            'id': item_id,
            'name': name,
            'category': category,
            'price': price,
            'stock': initial_stock
        }
        
        # Initialize stock history
        self.stock_history[item_id] = []
        if initial_stock > 0:
            self.stock_history[item_id].append({
                'timestamp': time.time(),
                'operation': 'initial',
                'quantity': initial_stock,
                'new_stock': initial_stock
            })
        
        return True
    
    def get_item(self, item_id):
        """Retrieve an item by its ID."""
        return self.items.get(item_id)
    
    def remove_item(self, item_id):
        """Remove an item from the inventory."""
        if item_id in self.items:
            del self.items[item_id]
            if item_id in self.stock_history:
                del self.stock_history[item_id]
            return True
        return False
    
    def list_all_items(self):
        """Get all items in the inventory."""
        return list(self.items.values())
    
    def get_item_count(self):
        """Get the total number of items in inventory."""
        return len(self.items)
    
    def get_items_by_category(self, category):
        """Get all items in a specific category."""
        return [item for item in self.items.values() 
                if item['category'] == category]
    
    def get_items_in_price_range(self, min_price, max_price):
        """Get items within a price range."""
        return [item for item in self.items.values() 
                if min_price <= item['price'] <= max_price]
    
    def search_items_by_name(self, query):
        """Search items by name (case-insensitive)."""
        query_lower = query.lower()
        return [item for item in self.items.values() 
                if query_lower in item['name'].lower()]
    
    def get_categories(self):
        """Get all unique categories."""
        categories = set(item['category'] for item in self.items.values())
        return sorted(list(categories))
    
    def get_price_stats(self):
        """Get price statistics."""
        if not self.items:
            return None
        
        prices = [item['price'] for item in self.items.values()]
        return {
            'min': min(prices),
            'max': max(prices),
            'average': sum(prices) / len(prices)
        }
    
    # =================== LEVEL 3 NEW METHODS ===================
    
    def update_stock(self, item_id, quantity, operation="add"):
        """Update stock for an item."""
        if item_id not in self.items:
            return False
        
        if operation == "add":
            self.items[item_id]['stock'] += quantity
        elif operation == "remove":
            if self.items[item_id]['stock'] < quantity:
                return False  # Can't remove more than available
            self.items[item_id]['stock'] -= quantity
        else:
            return False  # Invalid operation
        
        # Record stock movement
        self.stock_history[item_id].append({
            'timestamp': time.time(),
            'operation': operation,
            'quantity': quantity,
            'new_stock': self.items[item_id]['stock']
        })
        
        return True
    
    def get_low_stock_items(self, threshold):
        """Get items with stock below threshold."""
        return [item for item in self.items.values() 
                if item['stock'] < threshold]
    
    def get_total_inventory_value(self):
        """Calculate total inventory value."""
        return sum(item['price'] * item['stock'] for item in self.items.values())
    
    def get_stock_history(self, item_id):
        """Get stock movement history for an item."""
        return self.stock_history.get(item_id, [])
    
    def validate_sale(self, item_id, quantity):
        """Check if a sale is possible."""
        if item_id not in self.items:
            return False
        return self.items[item_id]['stock'] >= quantity
    
    def process_sale(self, item_id, quantity):
        """Process a sale (reduce stock, record transaction)."""
        if not self.validate_sale(item_id, quantity):
            return None
        
        item = self.items[item_id]
        old_stock = item['stock']
        
        # Update stock
        item['stock'] -= quantity
        
        # Record stock movement
        self.stock_history[item_id].append({
            'timestamp': time.time(),
            'operation': 'sale',
            'quantity': quantity,
            'new_stock': item['stock']
        })
        
        # Return sale details
        return {
            'item_id': item_id,
            'item_name': item['name'],
            'quantity_sold': quantity,
            'unit_price': item['price'],
            'total_amount': item['price'] * quantity,
            'remaining_stock': item['stock']
        }


if __name__ == "__main__":
    inventory = InventoryManager()
    
    # Test Level 3 functionality
    print("Testing Level 3 functionality...")
    
    # Add items with stock
    inventory.add_item("laptop1", "MacBook Pro", "Electronics", 2499.99, 10)
    inventory.add_item("mouse1", "Wireless Mouse", "Electronics", 79.99, 50)
    inventory.add_item("book1", "Python Guide", "Books", 39.99, 25)
    
    # Test stock operations
    inventory.update_stock("laptop1", 5, "add")
    print(f"Laptop stock after restock: {inventory.get_item('laptop1')['stock']}")
    
    # Test sales
    sale = inventory.process_sale("laptop1", 3)
    print(f"Sale processed: {sale}")
    
    # Test low stock
    low_stock = inventory.get_low_stock_items(20)
    print(f"Low stock items: {len(low_stock)}")
    
    # Test total value
    total_value = inventory.get_total_inventory_value()
    print(f"Total inventory value: ${total_value:.2f}")
    
    # Test history
    history = inventory.get_stock_history("laptop1")
    print(f"Laptop stock history: {len(history)} movements")
    
    print("✅ Level 3 implementation complete!")
