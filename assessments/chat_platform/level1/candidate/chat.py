"""
LEVEL 1: Basic Messaging
Implement core messaging operations.

Time Limit: 15-20 minutes
Points: ~100 points

Requirements:
- Register users with usernames
- Send messages between users
- Retrieve messages for users
- Basic message storage and user management
"""

from collections import defaultdict


class ChatPlatform:
    """
    Basic chat platform with messaging.
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize the chat platform
    - register_user(self, user_id, username): Register a new user
    - get_user(self, user_id): Get user information
    - send_message(self, from_user_id, to_user_id, content): Send a message
    - get_messages(self, user_id): Get all messages for a user
    - get_message_count(self, user_id): Count messages for a user
    - list_all_users(self): Get all registered users
    """
    
    def __init__(self):
        """Initialize the chat platform."""
        # TODO: Initialize storage for users and messages
        pass
    
    def register_user(self, user_id, username):
        """
        Register a new user.
        
        Args:
            user_id (str): Unique user identifier
            username (str): Display name for the user
            
        Returns:
            bool: True if registered successfully, False if user_id already exists
        """
        # TODO: Implement user registration
        pass
    
    def get_user(self, user_id):
        """
        Get user information.
        
        Args:
            user_id (str): User identifier
            
        Returns:
            dict: User data if found, None if not found
        """
        # TODO: Implement user retrieval
        pass
    
    def send_message(self, from_user_id, to_user_id, content):
        """
        Send a message from one user to another.
        
        Args:
            from_user_id (str): Sender's user ID
            to_user_id (str): Recipient's user ID
            content (str): Message content
            
        Returns:
            str: Message ID if successful, None if failed
        """
        # TODO: Implement message sending
        pass
    
    def get_messages(self, user_id):
        """
        Get all messages for a user.
        
        Args:
            user_id (str): User identifier
            
        Returns:
            list: List of messages received by the user
        """
        # TODO: Implement message retrieval
        pass
    
    def get_message_count(self, user_id):
        """
        Count messages for a user.
        
        Args:
            user_id (str): User identifier
            
        Returns:
            int: Number of messages (0 if user not found)
        """
        # TODO: Implement message counting
        pass
    
    def list_all_users(self):
        """
        Get all registered users.
        
        Returns:
            list: List of all user data
        """
        # TODO: Implement user listing
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    chat = ChatPlatform()
    print("Level 1: Implement the ChatPlatform class methods!")
