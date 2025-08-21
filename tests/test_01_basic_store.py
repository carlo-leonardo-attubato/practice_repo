"""
Unit Tests for Speed Drill 1: Basic Dictionary Operations
These tests will pass when you implement the Store class correctly.
"""

import pytest
import sys
import os

# Add the speed_drills directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'speed_drills'))

from basic_store import Store


class TestStore:
    """Test cases for Store class."""
    
    def setup_method(self):
        """Set up a fresh Store instance before each test."""
        self.store = Store()
    
    def test_initialization(self):
        """Test that Store initializes correctly."""
        assert self.store is not None
        assert hasattr(self.store, 'data')
    
    def test_set_basic(self):
        """Test basic set operation."""
        result = self.store.set("key1", "value1")
        assert result == "value1"
        assert self.store.data["key1"] == "value1"
    
    def test_get_existing(self):
        """Test getting an existing value."""
        self.store.set("key1", "value1")
        value = self.store.get("key1")
        assert value == "value1"
    
    def test_get_nonexistent(self):
        """Test getting a non-existent key."""
        value = self.store.get("nonexistent")
        assert value is None
    
    def test_delete_existing(self):
        """Test deleting an existing key."""
        self.store.set("key1", "value1")
        deleted_value = self.store.delete("key1")
        assert deleted_value == "value1"
        assert self.store.get("key1") is None
        assert "key1" not in self.store.data
    
    def test_delete_nonexistent(self):
        """Test deleting a non-existent key."""
        deleted_value = self.store.delete("nonexistent")
        assert deleted_value is None
    
    def test_multiple_operations(self):
        """Test multiple operations in sequence."""
        self.store.set("key1", "value1")
        self.store.set("key2", "value2")
        self.store.set("key1", "updated_value")
        
        assert self.store.get("key1") == "updated_value"
        assert self.store.get("key2") == "value2"
        
        self.store.delete("key1")
        assert self.store.get("key1") is None
        assert self.store.get("key2") == "value2"
    
    def test_overwrite_value(self):
        """Test that setting same key overwrites value."""
        self.store.set("key1", "old_value")
        self.store.set("key1", "new_value")
        
        assert self.store.get("key1") == "new_value"
        assert len(self.store.data) == 1
    
    def test_empty_store(self):
        """Test operations on empty store."""
        assert self.store.get("any_key") is None
        assert self.store.delete("any_key") is None
        assert len(self.store.data) == 0


def run_tests():
    """Run all tests and display results."""
    print("🧪 Speed Drill 1: Basic Dictionary Operations")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\nTo run tests manually, use:")
    print("python -m pytest tests/test_01_basic_store.py -v")


if __name__ == "__main__":
    run_tests()
