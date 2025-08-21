"""
LEVEL 4: Advanced Operations & Data Management - MODEL SOLUTION
Complete inventory system with backup/restore and batch operations.
"""

import time
import copy


class InventoryManager:
    """Complete inventory management system with advanced operations."""
    
    def __init__(self):
        """Initialize the inventory manager."""
        self.items = {}  # item_id -> item_data
        self.stock_history = {}  # item_id -> list of movements
        self.backups = {}  # backup_id -> complete state
    
    # =================== LEVEL 1-3 METHODS ===================
    
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
        return self.items.get(item_id)
    
    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            if item_id in self.stock_history:
                del self.stock_history[item_id]
            return True
        return False
    
    def list_all_items(self):
        return list(self.items.values())
    
    def get_item_count(self):
        return len(self.items)
    
    def get_items_by_category(self, category):
        return [item for item in self.items.values() if item['category'] == category]
    
    def get_items_in_price_range(self, min_price, max_price):
        return [item for item in self.items.values() if min_price <= item['price'] <= max_price]
    
    def search_items_by_name(self, query):
        query_lower = query.lower()
        return [item for item in self.items.values() if query_lower in item['name'].lower()]
    
    def get_categories(self):
        categories = set(item['category'] for item in self.items.values())
        return sorted(list(categories))
    
    def get_price_stats(self):
        if not self.items:
            return None
        prices = [item['price'] for item in self.items.values()]
        return {
            'min': min(prices),
            'max': max(prices),
            'average': sum(prices) / len(prices)
        }
    
    def update_stock(self, item_id, quantity, operation="add"):
        if item_id not in self.items:
            return False
        
        if operation == "add":
            self.items[item_id]['stock'] += quantity
        elif operation == "remove":
            if self.items[item_id]['stock'] < quantity:
                return False
            self.items[item_id]['stock'] -= quantity
        else:
            return False
        
        self.stock_history[item_id].append({
            'timestamp': time.time(),
            'operation': operation,
            'quantity': quantity,
            'new_stock': self.items[item_id]['stock']
        })
        
        return True
    
    def get_low_stock_items(self, threshold):
        return [item for item in self.items.values() if item['stock'] < threshold]
    
    def get_total_inventory_value(self):
        return sum(item['price'] * item['stock'] for item in self.items.values())
    
    def get_stock_history(self, item_id):
        return self.stock_history.get(item_id, [])
    
    def validate_sale(self, item_id, quantity):
        if item_id not in self.items:
            return False
        return self.items[item_id]['stock'] >= quantity
    
    def process_sale(self, item_id, quantity):
        if not self.validate_sale(item_id, quantity):
            return None
        
        item = self.items[item_id]
        item['stock'] -= quantity
        
        self.stock_history[item_id].append({
            'timestamp': time.time(),
            'operation': 'sale',
            'quantity': quantity,
            'new_stock': item['stock']
        })
        
        return {
            'item_id': item_id,
            'item_name': item['name'],
            'quantity_sold': quantity,
            'unit_price': item['price'],
            'total_amount': item['price'] * quantity,
            'remaining_stock': item['stock']
        }
    
    # =================== LEVEL 4 NEW METHODS ===================
    
    def backup_inventory(self, backup_id):
        """Create a complete backup of the inventory state."""
        self.backups[backup_id] = {
            'items': copy.deepcopy(self.items),
            'stock_history': copy.deepcopy(self.stock_history),
            'timestamp': time.time()
        }
        return True
    
    def restore_inventory(self, backup_id):
        """Restore inventory from a backup."""
        if backup_id not in self.backups:
            return False
        
        backup = self.backups[backup_id]
        self.items = copy.deepcopy(backup['items'])
        self.stock_history = copy.deepcopy(backup['stock_history'])
        return True
    
    def bulk_add_items(self, items_list):
        """Add multiple items at once."""
        added_count = 0
        failed_items = []
        
        for item_data in items_list:
            try:
                result = self.add_item(
                    item_data['id'],
                    item_data['name'],
                    item_data['category'],
                    item_data['price'],
                    item_data.get('stock', 0)
                )
                if result:
                    added_count += 1
                else:
                    failed_items.append(item_data['id'])
            except (KeyError, TypeError):
                failed_items.append(item_data.get('id', 'unknown'))
        
        return {
            'added': added_count,
            'failed': failed_items
        }
    
    def bulk_update_stock(self, updates_list):
        """Update stock for multiple items at once."""
        updated_count = 0
        failed_updates = []
        
        for update_data in updates_list:
            try:
                result = self.update_stock(
                    update_data['item_id'],
                    update_data['quantity'],
                    update_data.get('operation', 'add')
                )
                if result:
                    updated_count += 1
                else:
                    failed_updates.append(update_data['item_id'])
            except (KeyError, TypeError):
                failed_updates.append(update_data.get('item_id', 'unknown'))
        
        return {
            'updated': updated_count,
            'failed': failed_updates
        }
    
    def export_inventory(self):
        """Export entire inventory to dictionary format."""
        return {
            'items': copy.deepcopy(self.items),
            'stock_history': copy.deepcopy(self.stock_history),
            'export_timestamp': time.time(),
            'version': '1.0'
        }
    
    def import_inventory(self, data):
        """Import inventory from dictionary format."""
        try:
            if 'items' not in data:
                return False
            
            # Validate data structure
            for item_id, item_data in data['items'].items():
                required_fields = ['id', 'name', 'category', 'price', 'stock']
                if not all(field in item_data for field in required_fields):
                    return False
            
            # Import data
            self.items = copy.deepcopy(data['items'])
            self.stock_history = copy.deepcopy(data.get('stock_history', {}))
            
            return True
        except (KeyError, TypeError, AttributeError):
            return False
    
    def get_system_stats(self):
        """Get comprehensive system statistics."""
        if not self.items:
            return {
                'total_items': 0,
                'total_categories': 0,
                'total_stock_units': 0,
                'total_inventory_value': 0.0,
                'low_stock_items': 0,
                'total_backups': len(self.backups)
            }
        
        total_stock = sum(item['stock'] for item in self.items.values())
        total_value = self.get_total_inventory_value()
        low_stock_count = len(self.get_low_stock_items(10))
        
        return {
            'total_items': len(self.items),
            'total_categories': len(self.get_categories()),
            'total_stock_units': total_stock,
            'total_inventory_value': total_value,
            'low_stock_items': low_stock_count,
            'total_backups': len(self.backups),
            'average_stock_per_item': total_stock / len(self.items) if self.items else 0,
            'categories': self.get_categories()
        }


if __name__ == "__main__":
    inventory = InventoryManager()
    
    # Test Level 4 functionality
    print("Testing Level 4 functionality...")
    
    # Add items
    inventory.add_item("laptop1", "MacBook Pro", "Electronics", 2499.99, 10)
    inventory.add_item("mouse1", "Wireless Mouse", "Electronics", 79.99, 50)
    
    # Create backup
    inventory.backup_inventory("backup1")
    print("✅ Backup created")
    
    # Make changes
    inventory.process_sale("laptop1", 5)
    inventory.update_stock("mouse1", 20, "add")
    
    # Test bulk operations
    bulk_items = [
        {'id': 'bulk1', 'name': 'Item 1', 'category': 'Test', 'price': 10.0, 'stock': 5},
        {'id': 'bulk2', 'name': 'Item 2', 'category': 'Test', 'price': 20.0, 'stock': 10}
    ]
    bulk_result = inventory.bulk_add_items(bulk_items)
    print(f"Bulk add result: {bulk_result}")
    
    # Test export
    exported_data = inventory.export_inventory()
    print(f"Exported {len(exported_data['items'])} items")
    
    # Test restore
    inventory.restore_inventory("backup1")
    print("✅ Restored from backup")
    
    # Test system stats
    stats = inventory.get_system_stats()
    print(f"System stats: {stats}")
    
    print("✅ Level 4 implementation complete!")