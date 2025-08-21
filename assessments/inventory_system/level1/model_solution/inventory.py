"""
LEVEL 1: Basic Inventory Management - MODEL SOLUTION
Basic CRUD operations for inventory items.
"""


class InventoryManager:
    """Basic inventory management system."""
    
    def __init__(self):
        """Initialize the inventory manager."""
        self.items = {}  # item_id -> item_data
    
    def add_item(self, item_id, name, category, price):
        """Add a new item to the inventory."""
        if item_id in self.items:
            return False
        
        self.items[item_id] = {
            'id': item_id,
            'name': name,
            'category': category,
            'price': price
        }
        return True
    
    def get_item(self, item_id):
        """Retrieve an item by its ID."""
        return self.items.get(item_id)
    
    def remove_item(self, item_id):
        """Remove an item from the inventory."""
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False
    
    def list_all_items(self):
        """Get all items in the inventory."""
        return list(self.items.values())
    
    def get_item_count(self):
        """Get the total number of items in inventory."""
        return len(self.items)


if __name__ == "__main__":
    inventory = InventoryManager()
    
    # Test the implementation
    print("Testing Level 1 functionality...")
    
    # Add items
    inventory.add_item("item1", "Laptop", "Electronics", 999.99)
    inventory.add_item("item2", "Mouse", "Electronics", 29.99)
    
    # Test retrieval
    item = inventory.get_item("item1")
    print(f"Retrieved item: {item}")
    
    # Test listing
    all_items = inventory.list_all_items()
    print(f"All items: {len(all_items)} items")
    
    # Test count
    count = inventory.get_item_count()
    print(f"Item count: {count}")
    
    # Test removal
    removed = inventory.remove_item("item1")
    print(f"Removed item1: {removed}")
    print(f"New count: {inventory.get_item_count()}")
    
    print("✅ Level 1 implementation complete!")
