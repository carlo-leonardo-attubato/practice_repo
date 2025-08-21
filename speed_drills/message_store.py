"""
Speed Drill: MessageStore Implementation
Complete this class to pass all tests.
"""

import time
from typing import List, Optional


class MessageStore:
    """
    A message storage system that supports:
    - Adding messages for users
    - Retrieving messages for users
    - Cleaning up old messages based on age
    """
    
    def __init__(self):
        """Initialize the message store."""
        # TODO: Implement storage structure
        pass
    
    def add_message(self, user_id: str, message: str) -> bool:
        """
        Add a message for a specific user.
        
        Args:
            user_id: The user identifier
            message: The message content
            
        Returns:
            True if message was added successfully
        """
        # TODO: Implement message addition with timestamp
        pass
    
    def get_messages(self, user_id: str) -> List[str]:
        """
        Get all messages for a specific user.
        
        Args:
            user_id: The user identifier
            
        Returns:
            List of messages for the user (empty if no messages)
        """
        # TODO: Implement message retrieval
        pass
    
    def cleanup(self, seconds_old: int) -> int:
        """
        Remove all messages older than specified seconds.
        
        Args:
            seconds_old: Messages older than this many seconds will be removed
            
        Returns:
            Number of messages removed
        """
        # TODO: Implement cleanup logic
        pass
    
    def get_message_count(self, user_id: str) -> int:
        """
        Get the total number of messages for a user.
        
        Args:
            user_id: The user identifier
            
        Returns:
            Number of messages for the user
        """
        # TODO: Implement message counting
        pass


# Test runner - uncomment to test your implementation
if __name__ == "__main__":
    # Quick test to see if your implementation works
    store = MessageStore()
    
    # Test basic functionality
    store.add_message("user1", "Hello!")
    store.add_message("user1", "How are you?")
    
    messages = store.get_messages("user1")
    print(f"User1 messages: {messages}")
    print(f"Message count: {store.get_message_count('user1')}")
    
    # Test cleanup
    removed = store.cleanup(0)  # Remove all messages
    print(f"Removed {removed} messages")
    print(f"After cleanup: {store.get_messages('user1')}")
