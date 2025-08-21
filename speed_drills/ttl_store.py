"""
SPEED DRILL 3: Time-based Operations (TTL Pattern)
Implement the TTLStore class to pass all tests.
"""

import time


class TTLStore:
    """
    A key-value store with automatic expiration (TTL).
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize storage
    - set(self, key, value, ttl_seconds): Set with expiration
    - get(self, key): Get if not expired, None if expired
    - delete(self, key): Manual deletion
    - get_all_keys(self): Get all non-expired keys
    - cleanup_expired(self): Remove all expired items
    """
    
    def __init__(self):
        """Initialize the TTL store."""
        # TODO: Implement storage for data and expiry times
        pass
    
    def set(self, key, value, ttl_seconds):
        """Set a key-value pair with expiration time."""
        # TODO: Store value and calculate expiry timestamp
        pass
    
    def get(self, key):
        """Get value if not expired, return None if expired."""
        # TODO: Check expiry and return value or None
        pass
    
    def delete(self, key):
        """Manually delete a key-value pair."""
        # TODO: Implement deletion
        pass
    
    def get_all_keys(self):
        """Get all non-expired keys."""
        # TODO: Return list of valid keys
        pass
    
    def cleanup_expired(self):
        """Remove all expired items. Return count removed."""
        # TODO: Implement cleanup logic
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    store = TTLStore()
    print("Implement the TTLStore class methods first!")
