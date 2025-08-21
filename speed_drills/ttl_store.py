"""
Speed Drill: TTL Store Implementation
Implement a key-value store with automatic expiration.
"""

import time
from typing import Any, Optional


class TTLStore:
    """
    A key-value store where values automatically expire after a specified time.
    """
    
    def __init__(self):
        """Initialize the TTL store."""
        # TODO: Implement storage structure
        pass
    
    def set(self, key: str, value: Any, ttl_seconds: int) -> bool:
        """
        Set a key-value pair with expiration time.
        
        Args:
            key: The key
            value: The value to store
            ttl_seconds: Time to live in seconds
            
        Returns:
            True if set successfully
        """
        # TODO: Implement TTL set
        pass
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get a value by key if it hasn't expired.
        
        Args:
            key: The key to retrieve
            
        Returns:
            The value if not expired, None otherwise
        """
        # TODO: Implement TTL get with expiration check
        pass
    
    def delete(self, key: str) -> bool:
        """
        Delete a key-value pair.
        
        Args:
            key: The key to delete
            
        Returns:
            True if deleted, False if key didn't exist
        """
        # TODO: Implement delete
        pass
    
    def get_all_keys(self) -> list[str]:
        """
        Get all non-expired keys.
        
        Returns:
            List of valid keys
        """
        # TODO: Implement key listing with expiration check
        pass
    
    def cleanup_expired(self) -> int:
        """
        Remove all expired key-value pairs.
        
        Returns:
            Number of expired items removed
        """
        # TODO: Implement cleanup
        pass


# Test your implementation
if __name__ == "__main__":
    store = TTLStore()
    
    # Test basic TTL functionality
    store.set("key1", "value1", 1)  # Expires in 1 second
    print(f"Get key1: {store.get('key1')}")
    
    # Wait for expiration
    time.sleep(1.1)
    print(f"Get key1 after expiration: {store.get('key1')}")
    
    # Test cleanup
    store.set("key2", "value2", 0)  # Expires immediately
    removed = store.cleanup_expired()
    print(f"Cleaned up {removed} expired items")
