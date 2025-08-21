"""
Unit Tests for Speed Drill 5: Backup/Restore Operations
These tests will pass when you implement the Database class correctly.
"""

import pytest
import sys
import os

# Add the speed_drills directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'speed_drills'))

from speed_drills.backup_restore import Database


class TestDatabase:
    """Test cases for Database class."""
    
    def setup_method(self):
        """Set up a fresh Database instance before each test."""
        self.db = Database()
    
    def test_initialization(self):
        """Test that Database initializes correctly."""
        assert self.db is not None
        assert hasattr(self.db, 'data')
        assert hasattr(self.db, 'backups')
    
    def test_set_basic(self):
        """Test basic set operation."""
        self.db.set("key1", "value1")
        assert self.db.data["key1"] == "value1"
    
    def test_set_multiple(self):
        """Test setting multiple key-value pairs."""
        self.db.set("key1", "value1")
        self.db.set("key2", "value2")
        self.db.set("key3", "value3")
        
        assert self.db.data["key1"] == "value1"
        assert self.db.data["key2"] == "value2"
        assert self.db.data["key3"] == "value3"
    
    def test_set_overwrite(self):
        """Test that setting same key overwrites value."""
        self.db.set("key1", "old_value")
        self.db.set("key1", "new_value")
        
        assert self.db.data["key1"] == "new_value"
        assert len(self.db.data) == 1
    
    def test_backup_basic(self):
        """Test basic backup creation."""
        self.db.set("key1", "value1")
        self.db.set("key2", "value2")
        
        result = self.db.backup("backup1")
        assert result is None  # Method doesn't return anything
        
        assert "backup1" in self.db.backups
        assert self.db.backups["backup1"]["key1"] == "value1"
        assert self.db.backups["backup1"]["key2"] == "value2"
    
    def test_backup_multiple(self):
        """Test creating multiple backups."""
        self.db.set("key1", "value1")
        self.db.backup("backup1")
        
        self.db.set("key2", "value2")
        self.db.backup("backup2")
        
        assert len(self.db.backups) == 2
        assert "backup1" in self.db.backups
        assert "backup2" in self.db.backups
        
        # backup1 should only have key1
        assert "key1" in self.db.backups["backup1"]
        assert "key2" not in self.db.backups["backup1"]
        
        # backup2 should have both keys
        assert "key1" in self.db.backups["backup2"]
        assert "key2" in self.db.backups["backup2"]
    
    def test_restore_existing(self):
        """Test restoring from existing backup."""
        self.db.set("key1", "value1")
        self.db.backup("backup1")
        
        # Modify data
        self.db.set("key1", "modified_value")
        self.db.set("key2", "new_value")
        
        # Restore
        result = self.db.restore("backup1")
        assert result is True
        
        # Should be back to backup state
        assert self.db.data["key1"] == "value1"
        assert "key2" not in self.db.data
        assert len(self.db.data) == 1
    
    def test_restore_nonexistent(self):
        """Test restoring from non-existent backup."""
        result = self.db.restore("nonexistent")
        assert result is False
        
        # Data should remain unchanged
        assert len(self.db.data) == 0
    
    def test_backup_restore_workflow(self):
        """Test complete backup/restore workflow."""
        # Initial state
        self.db.set("key1", "initial_value")
        self.db.backup("initial")
        
        # Make changes
        self.db.set("key1", "changed_value")
        self.db.set("key2", "new_key")
        self.db.backup("modified")
        
        # Restore to initial
        self.db.restore("initial")
        assert self.db.data["key1"] == "initial_value"
        assert "key2" not in self.db.data
        
        # Restore to modified
        self.db.restore("modified")
        assert self.db.data["key1"] == "changed_value"
        assert self.db.data["key2"] == "new_key"
    
    def test_backup_independence(self):
        """Test that backups are independent of each other."""
        self.db.set("key1", "value1")
        self.db.backup("backup1")
        
        self.db.set("key1", "value2")
        self.db.backup("backup2")
        
        # Restore backup1
        self.db.restore("backup1")
        assert self.db.data["key1"] == "value1"
        
        # Restore backup2
        self.db.restore("backup2")
        assert self.db.data["key1"] == "value2"
    
    def test_complex_data_types(self):
        """Test backing up and restoring complex data types."""
        # Nested dictionary
        nested_data = {
            "users": {
                "user1": {"name": "Alice", "age": 25},
                "user2": {"name": "Bob", "age": 30}
            },
            "settings": {"theme": "dark", "notifications": True}
        }
        
        self.db.set("config", nested_data)
        self.db.backup("complex_backup")
        
        # Modify the data
        self.db.set("config", {"modified": True})
        
        # Restore
        self.db.restore("complex_backup")
        restored_config = self.db.data["config"]
        
        assert restored_config["users"]["user1"]["name"] == "Alice"
        assert restored_config["users"]["user2"]["age"] == 30
        assert restored_config["settings"]["theme"] == "dark"
    
    def test_edge_cases(self):
        """Test edge cases and error handling."""
        # Empty backup
        self.db.backup("empty_backup")
        assert "empty_backup" in self.db.backups
        assert len(self.db.backups["empty_backup"]) == 0
        
        # Restore empty backup
        self.db.set("key1", "value1")
        self.db.restore("empty_backup")
        assert len(self.db.data) == 0
        
        # Very long backup ID
        long_id = "x" * 1000
        self.db.set("key1", "value1")
        self.db.backup(long_id)
        assert long_id in self.db.backups
        
        # Restore from long ID
        self.db.set("key2", "value2")
        result = self.db.restore(long_id)
        assert result is True
        assert "key1" in self.db.data
        assert "key2" not in self.db.data


def run_tests():
    """Run all tests and display results."""
    print("🧪 Speed Drill 5: Backup/Restore Operations")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\nTo run tests manually, use:")
    print("python -m pytest tests/test_05_backup_restore.py -v")


if __name__ == "__main__":
    run_tests()
