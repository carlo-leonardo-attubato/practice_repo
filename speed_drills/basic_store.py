"""
SPEED DRILL 1: Basic Dictionary Operations
Implement the Store class to pass all tests.
"""


class Store:
    """
    A simple key-value store with basic CRUD operations.
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize storage
    - set(self, key, value): Store a key-value pair  
    - get(self, key): Retrieve a value by key
    - delete(self, key): Remove a key-value pair
    """
    
    def __init__(self):
        """Initialize the store."""
        self.data = {}
    
    def set(self, key, value):
        """Store a key-value pair. Return the value stored."""
        self.data[key] = value
        return value
    
    def get(self, key):
        """Retrieve a value by key. Return None if not found."""
        return self.data.get(key)
    
    def delete(self, key):
        """Remove a key-value pair. Return deleted value or None."""
        if key in self.data:
            value = self.data[key]
            del self.data[key]
            return value
        return None


# Quick test - uncomment when ready
if __name__ == "__main__":
    store = Store()
    print("Store class implemented!")
    
    # Test basic functionality
    store.set("key1", "value1")
    print(f"Get key1: {store.get('key1')}")
    
    store.set("key2", "value2")
    print(f"Get key2: {store.get('key2')}")
    
    deleted = store.delete("key1")
    print(f"Deleted key1: {deleted}")
    print(f"Get key1 after delete: {store.get('key1')}")
    
    print(f"Final store contents: {store.data}")
