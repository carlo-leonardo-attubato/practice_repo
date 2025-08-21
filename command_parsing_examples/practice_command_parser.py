"""
PRACTICE: Command Parsing Pattern
Practice converting the weird command format to familiar OOP.
"""

import time
from datetime import datetime


class InventoryCommandSystem:
    """
    Example: Convert inventory commands to familiar OOP.
    This shows the pattern for ANY domain (inventory, chat, banking, etc.)
    """
    
    def __init__(self):
        self.items = {}  # item_id -> item_data
        self.history = []  # For rollback
    
    def add_item(self, item_id: str, name: str, price: float, timestamp: float = None):
        """Add item - familiar OOP method."""
        current_time = timestamp or time.time()
        
        self.items[item_id] = {
            'id': item_id,
            'name': name,
            'price': price,
            'added_at': current_time
        }
        
        self.history.append({
            'action': 'add',
            'item_id': item_id,
            'timestamp': current_time,
            'data': self.items[item_id].copy()
        })
        
        return f"added{' at' if timestamp else ''} {item_id}"
    
    def get_item(self, item_id: str, timestamp: float = None):
        """Get item - familiar OOP method."""
        if item_id not in self.items:
            return "item not found"
        
        item = self.items[item_id]
        return f"got{' at' if timestamp else ''} {item['name']} (${item['price']:.2f})"
    
    def search_items(self, query: str, timestamp: float = None):
        """Search items - familiar OOP method."""
        matching_items = []
        for item_id, item_data in self.items.items():
            if query.lower() in item_data['name'].lower():
                matching_items.append(item_id)
        
        matching_items.sort()
        return f"found{' at' if timestamp else ''} {matching_items}"
    
    def rollback_to_time(self, target_time: float):
        """Rollback - familiar OOP method."""
        # Remove items added after target time
        items_to_remove = []
        for item_id, item_data in self.items.items():
            if item_data['added_at'] > target_time:
                items_to_remove.append(item_id)
        
        for item_id in items_to_remove:
            del self.items[item_id]
        
        return f"rollback to {datetime.fromtimestamp(target_time).strftime('%Y-%m-%dT%H:%M:%S')}"


def parse_inventory_commands(commands):
    """
    THE COMMAND PARSER - This is what you need to write in CodeSignal.
    """
    
    system = InventoryCommandSystem()
    results = []
    
    for command in commands:
        cmd_type = command[0]
        
        if cmd_type == "ADD_ITEM":
            # ["ADD_ITEM", "item1", "Laptop", "999.99"]
            item_id, name, price_str = command[1], command[2], command[3]
            result = system.add_item(item_id, name, float(price_str))
            results.append(result)
            
        elif cmd_type == "GET_ITEM":
            # ["GET_ITEM", "item1"]
            item_id = command[1]
            result = system.get_item(item_id)
            results.append(result)
            
        elif cmd_type == "SEARCH_ITEMS":
            # ["SEARCH_ITEMS", "Lap"]
            query = command[1]
            result = system.search_items(query)
            results.append(result)
            
        elif cmd_type == "ADD_ITEM_AT":
            # ["ADD_ITEM_AT", "2021-07-01T12:00:00", "item2", "Mouse", "29.99"]
            timestamp_str, item_id, name, price_str = command[1], command[2], command[3], command[4]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            result = system.add_item(item_id, name, float(price_str), timestamp)
            results.append(result)
            
        elif cmd_type == "ROLLBACK":
            # ["ROLLBACK", "2021-07-01T12:10:00"]
            timestamp_str = command[1]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            result = system.rollback_to_time(timestamp)
            results.append(result)
    
    return results


# =================== THE TEMPLATE YOU NEED ===================

def anthropic_codesignal_template(commands):
    """
    COPY THIS TEMPLATE for tomorrow's assessment!
    
    Just replace:
    1. The class name (FileSystem → YourDomain)
    2. The methods (upload_file → your_methods)
    3. The command types (FILE_UPLOAD → YOUR_COMMANDS)
    """
    
    # Step 1: Create your familiar OOP class
    system = YourDomainClass()  # ← Replace with your domain
    results = []
    
    # Step 2: Parse each command
    for command in commands:
        cmd_type = command[0]
        
        # Step 3: Convert command to method call
        if cmd_type == "YOUR_COMMAND_TYPE":  # ← Replace with actual commands
            # Extract parameters from command
            param1, param2 = command[1], command[2]
            
            # Call your familiar OOP method
            result = system.your_method(param1, param2)  # ← Your method
            results.append(result)
        
        # Add more command types as needed...
    
    return results


if __name__ == "__main__":
    print("🎯 COMMAND PARSING PRACTICE")
    print("="*50)
    
    # Test inventory command parsing
    test_commands = [
        ["ADD_ITEM", "laptop1", "MacBook Pro", "2499.99"],
        ["ADD_ITEM", "mouse1", "Wireless Mouse", "79.99"],
        ["GET_ITEM", "laptop1"],
        ["SEARCH_ITEMS", "Mac"],
        ["ROLLBACK", "2021-07-01T12:05:00"]
    ]
    
    print("Commands:", test_commands)
    print()
    
    results = parse_inventory_commands(test_commands)
    print("Results:")
    for i, result in enumerate(results):
        print(f"  {i+1}. {result}")
    
    print("\n✅ Master this pattern and you'll crush tomorrow's assessment!")
    print("The key: Commands are just a weird way to call your familiar OOP methods!")
