"""
Unit Tests for Speed Drill 2: Nested Dictionary Pattern
These tests will pass when you implement the UserStore class correctly.
"""

import pytest
import sys
import os

# Add the speed_drills directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'speed_drills'))

from speed_drills.nested_userstore import UserStore


class TestUserStore:
    """Test cases for UserStore class."""
    
    def setup_method(self):
        """Set up a fresh UserStore instance before each test."""
        self.store = UserStore()
    
    def test_initialization(self):
        """Test that UserStore initializes correctly."""
        assert self.store is not None
        assert hasattr(self.store, 'users')
    
    def test_add_user_field_basic(self):
        """Test basic user field addition."""
        result = self.store.add_user_field("user1", "name", "Alice")
        assert result is None  # Method doesn't return anything
        assert "user1" in self.store.users
        assert self.store.users["user1"]["name"] == "Alice"
    
    def test_add_user_field_multiple(self):
        """Test adding multiple fields to a user."""
        self.store.add_user_field("user1", "name", "Alice")
        self.store.add_user_field("user1", "age", 25)
        self.store.add_user_field("user1", "city", "NYC")
        
        user_data = self.store.users["user1"]
        assert user_data["name"] == "Alice"
        assert user_data["age"] == 25
        assert user_data["city"] == "NYC"
    
    def test_add_user_field_multiple_users(self):
        """Test adding fields to multiple users."""
        self.store.add_user_field("user1", "name", "Alice")
        self.store.add_user_field("user2", "name", "Bob")
        
        assert self.store.users["user1"]["name"] == "Alice"
        assert self.store.users["user2"]["name"] == "Bob"
    
    def test_get_user_field_existing(self):
        """Test getting an existing user field."""
        self.store.add_user_field("user1", "name", "Alice")
        value = self.store.get_user_field("user1", "name")
        assert value == "Alice"
    
    def test_get_user_field_nonexistent_user(self):
        """Test getting field from non-existent user."""
        value = self.store.get_user_field("nonexistent", "name")
        assert value is None
    
    def test_get_user_field_nonexistent_field(self):
        """Test getting non-existent field from existing user."""
        self.store.add_user_field("user1", "name", "Alice")
        value = self.store.get_user_field("user1", "age")
        assert value is None
    
    def test_get_all_users_with_field_exact_match(self):
        """Test finding users with exact field value match."""
        self.store.add_user_field("user1", "role", "admin")
        self.store.add_user_field("user2", "role", "user")
        self.store.add_user_field("user3", "role", "admin")
        
        admin_users = self.store.get_all_users_with_field("role", "admin")
        assert len(admin_users) == 2
        assert "user1" in admin_users
        assert "user3" in admin_users
    
    def test_get_all_users_with_field_no_matches(self):
        """Test finding users when no matches exist."""
        self.store.add_user_field("user1", "role", "admin")
        
        user_users = self.store.get_all_users_with_field("role", "user")
        assert len(user_users) == 0
    
    def test_get_all_users_with_field_empty_store(self):
        """Test finding users in empty store."""
        users = self.store.get_all_users_with_field("role", "admin")
        assert len(users) == 0
    
    def test_overwrite_user_field(self):
        """Test that adding same field overwrites value."""
        self.store.add_user_field("user1", "name", "Alice")
        self.store.add_user_field("user1", "name", "Alicia")
        
        value = self.store.get_user_field("user1", "name")
        assert value == "Alicia"
    
    def test_complex_data_types(self):
        """Test storing complex data types in user fields."""
        self.store.add_user_field("user1", "scores", [85, 92, 78])
        self.store.add_user_field("user1", "metadata", {"verified": True, "level": "premium"})
        
        scores = self.store.get_user_field("user1", "scores")
        metadata = self.store.get_user_field("user1", "metadata")
        
        assert scores == [85, 92, 78]
        assert metadata["verified"] is True
        assert metadata["level"] == "premium"


def run_tests():
    """Run all tests and display results."""
    print("🧪 Speed Drill 2: Nested Dictionary Pattern")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\nTo run tests manually, use:")
    print("python -m pytest tests/test_02_nested_userstore.py -v")


if __name__ == "__main__":
    run_tests()
