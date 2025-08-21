"""
LEVEL 2: Enhanced Inventory Management - MODEL SOLUTION
Enhanced features with filtering and search capabilities.
"""


class InventoryManager:
    """Enhanced inventory management system with filtering and search."""
    
    def __init__(self):
        """Initialize the inventory manager."""
        self.items = {}  # item_id -> item_data
    
    # =================== LEVEL 1 METHODS ===================
    
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
    
    # =================== LEVEL 2 NEW METHODS ===================
    
    def get_items_by_category(self, category):
        """Get all items in a specific category."""
        return [item for item in self.items.values() 
                if item['category'] == category]
    
    def get_items_in_price_range(self, min_price, max_price):
        """Get items within a price range (inclusive)."""
        return [item for item in self.items.values() 
                if min_price <= item['price'] <= max_price]
    
    def search_items_by_name(self, query):
        """Search items by name (case-insensitive partial match)."""
        query_lower = query.lower()
        return [item for item in self.items.values() 
                if query_lower in item['name'].lower()]
    
    def get_categories(self):
        """Get all unique categories in the inventory."""
        categories = set(item['category'] for item in self.items.values())
        return sorted(list(categories))
    
    def get_price_stats(self):
        """Get price statistics for all items."""
        if not self.items:
            return None
        
        prices = [item['price'] for item in self.items.values()]
        return {
            'min': min(prices),
            'max': max(prices),
            'average': sum(prices) / len(prices)
        }


if __name__ == "__main__":
    inventory = InventoryManager()
    
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
