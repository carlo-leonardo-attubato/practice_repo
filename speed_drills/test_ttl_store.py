"""
Test suite for TTLStore implementation.
Run this to verify your implementation works correctly.
"""

import time
import pytest
from ttl_store import TTLStore


class TestTTLStore:
    """Test cases for TTLStore class."""
    
    def setup_method(self):
        """Set up a fresh TTLStore instance before each test."""
        self.store = TTLStore()
    
    def test_initialization(self):
        """Test that TTLStore initializes correctly."""
        assert self.store is not None
    
    def test_set_basic(self):
        """Test basic set operation."""
        result = self.store.set("key1", "value1", 60)
        assert result is True
        
        value = self.store.get("key1")
        assert value == "value1"
    
    def test_get_expired(self):
        """Test that expired values return None."""
        self.store.set("key1", "value1", 0)  # Expires immediately
        
        # Should be None since it expired
        value = self.store.get("key1")
        assert value is None
    
    def test_get_not_expired(self):
        """Test that non-expired values are returned."""
        self.store.set("key1", "value1", 10)  # Expires in 10 seconds
        
        value = self.store.get("key1")
        assert value == "value1"
    
    def test_delete_existing(self):
        """Test deleting an existing key."""
        self.store.set("key1", "value1", 60)
        
        result = self.store.delete("key1")
        assert result is True
        
        # Should return None after deletion
        value = self.store.get("key1")
        assert value is None
    
    def test_delete_nonexistent(self):
        """Test deleting a non-existent key."""
        result = self.store.delete("nonexistent")
        assert result is False
    
    def test_get_all_keys_no_expired(self):
        """Test getting all keys when none are expired."""
        self.store.set("key1", "value1", 60)
        self.store.set("key2", "value2", 60)
        
        keys = self.store.get_all_keys()
        assert len(keys) == 2
        assert "key1" in keys
        assert "key2" in keys
    
    def test_get_all_keys_with_expired(self):
        """Test getting all keys excludes expired ones."""
        self.store.set("key1", "value1", 0)  # Expires immediately
        self.store.set("key2", "value2", 60)  # Valid
        
        keys = self.store.get_all_keys()
        assert len(keys) == 1
        assert "key2" in keys
        assert "key1" not in keys
    
    def test_cleanup_expired(self):
        """Test cleanup removes expired items."""
        self.store.set("key1", "value1", 0)  # Expires immediately
        self.store.set("key2", "value2", 60)  # Valid
        
        removed = self.store.cleanup_expired()
        assert removed == 1
        
        # Check remaining keys
        keys = self.store.get_all_keys()
        assert len(keys) == 1
        assert "key2" in keys
    
    def test_cleanup_no_expired(self):
        """Test cleanup when no items are expired."""
        self.store.set("key1", "value1", 60)
        self.store.set("key2", "value2", 60)
        
        removed = self.store.cleanup_expired()
        assert removed == 0
        
        keys = self.store.get_all_keys()
        assert len(keys) == 2
    
    def test_ttl_accuracy(self):
        """Test TTL timing accuracy."""
        self.store.set("key1", "value1", 1)  # Expires in 1 second
        
        # Should be available immediately
        assert self.store.get("key1") == "value1"
        
        # Wait for expiration
        time.sleep(1.1)
        
        # Should be expired
        assert self.store.get("key1") is None
    
    def test_multiple_sets_same_key(self):
        """Test setting the same key multiple times."""
        self.store.set("key1", "value1", 60)
        self.store.set("key1", "value2", 60)
        
        value = self.store.get("key1")
        assert value == "value2"  # Should get the latest value
    
    def test_edge_cases(self):
        """Test edge cases and error handling."""
        # Empty string key and value
        result = self.store.set("", "", 60)
        assert result is True
        
        # Very long key and value
        long_key = "x" * 1000
        long_value = "y" * 1000
        result = self.store.set(long_key, long_value, 60)
        assert result is True
        
        # Negative TTL (should still work, just expire immediately)
        self.store.set("key1", "value1", -1)
        assert self.store.get("key1") is None
    
    def test_complex_data_types(self):
        """Test storing complex data types."""
        # List
        self.store.set("list_key", [1, 2, 3], 60)
        assert self.store.get("list_key") == [1, 2, 3]
        
        # Dictionary
        self.store.set("dict_key", {"a": 1, "b": 2}, 60)
        assert self.store.get("dict_key") == {"a": 1, "b": 2}
        
        # Nested structure
        nested = {"users": [{"id": 1, "name": "Alice"}]}
        self.store.set("nested_key", nested, 60)
        assert self.store.get("nested_key") == nested


def run_tests():
    """Run all tests and display results."""
    print("🧪 Running TTLStore tests...")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\nTo run tests manually, use:")
    print("python -m pytest speed_drills/test_ttl_store.py -v")


if __name__ == "__main__":
    run_tests()
