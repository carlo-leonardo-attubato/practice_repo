"""
Test suite for MessageStore implementation.
Run this to verify your implementation works correctly.
"""

import time
import pytest
from message_store import MessageStore


class TestMessageStore:
    """Test cases for MessageStore class."""
    
    def setup_method(self):
        """Set up a fresh MessageStore instance before each test."""
        self.store = MessageStore()
    
    def test_initialization(self):
        """Test that MessageStore initializes correctly."""
        assert self.store is not None
    
    def test_add_message_basic(self):
        """Test basic message addition."""
        result = self.store.add_message("user1", "Hello world!")
        assert result is True
        
        messages = self.store.get_messages("user1")
        assert "Hello world!" in messages
    
    def test_get_messages_empty_user(self):
        """Test getting messages for user with no messages."""
        messages = self.store.get_messages("nonexistent_user")
        assert messages == []
    
    def test_multiple_messages_same_user(self):
        """Test adding multiple messages for the same user."""
        self.store.add_message("user1", "First message")
        self.store.add_message("user1", "Second message")
        self.store.add_message("user1", "Third message")
        
        messages = self.store.get_messages("user1")
        assert len(messages) == 3
        assert "First message" in messages
        assert "Second message" in messages
        assert "Third message" in messages
    
    def test_multiple_users(self):
        """Test messages for different users are isolated."""
        self.store.add_message("user1", "User 1 message")
        self.store.add_message("user2", "User 2 message")
        
        user1_messages = self.store.get_messages("user1")
        user2_messages = self.store.get_messages("user2")
        
        assert user1_messages == ["User 1 message"]
        assert user2_messages == ["User 2 message"]
    
    def test_get_message_count(self):
        """Test message counting functionality."""
        assert self.store.get_message_count("user1") == 0
        
        self.store.add_message("user1", "Message 1")
        assert self.store.get_message_count("user1") == 1
        
        self.store.add_message("user1", "Message 2")
        assert self.store.get_message_count("user1") == 2
    
    def test_cleanup_no_messages(self):
        """Test cleanup when no messages exist."""
        removed = self.store.cleanup(60)
        assert removed == 0
    
    def test_cleanup_all_messages(self):
        """Test cleanup removes all messages when threshold is 0."""
        self.store.add_message("user1", "Message 1")
        self.store.add_message("user2", "Message 2")
        
        removed = self.store.cleanup(0)
        assert removed == 2
        
        assert self.store.get_messages("user1") == []
        assert self.store.get_messages("user2") == []
    
    def test_cleanup_partial_messages(self):
        """Test cleanup removes only old messages."""
        # Add messages with different timestamps
        self.store.add_message("user1", "Old message")
        
        # Wait a bit to create time difference
        time.sleep(0.1)
        
        self.store.add_message("user1", "New message")
        
        # Clean up messages older than 0.05 seconds
        removed = self.store.cleanup(0.05)
        assert removed == 1
        
        remaining = self.store.get_messages("user1")
        assert len(remaining) == 1
        assert "New message" in remaining
    
    def test_message_persistence_after_cleanup(self):
        """Test that remaining messages are still accessible after cleanup."""
        self.store.add_message("user1", "Persistent message")
        time.sleep(0.1)
        
        # Clean up old messages (but this one should remain)
        removed = self.store.cleanup(0.2)
        assert removed == 0
        
        messages = self.store.get_messages("user1")
        assert len(messages) == 1
        assert "Persistent message" in messages
    
    def test_edge_cases(self):
        """Test edge cases and error handling."""
        # Empty string message
        result = self.store.add_message("user1", "")
        assert result is True
        messages = self.store.get_messages("user1")
        assert "" in messages
        
        # Very long message
        long_message = "x" * 1000
        result = self.store.add_message("user1", long_message)
        assert result is True
        
        # Special characters
        special_message = "Hello! @#$%^&*()_+-=[]{}|;':\",./<>?"
        result = self.store.add_message("user1", special_message)
        assert result is True


def run_tests():
    """Run all tests and display results."""
    print("🧪 Running MessageStore tests...")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\nTo run tests manually, use:")
    print("python -m pytest speed_drills/test_message_store.py -v")


if __name__ == "__main__":
    run_tests()
