"""
LEVEL 1: Basic Messaging - MODEL SOLUTION
Core message operations and user management.
"""

import time
from collections import defaultdict


class ChatPlatform:
    """Basic chat platform with messaging."""
    
    def __init__(self):
        """Initialize the chat platform."""
        self.users = {}  # user_id -> user_data
        self.messages = defaultdict(list)  # user_id -> messages_received
        self.message_id_counter = 1
    
    def register_user(self, user_id, username):
        """Register a new user."""
        if user_id in self.users:
            return False
        
        self.users[user_id] = {
            'user_id': user_id,
            'username': username,
            'registered_at': time.time()
        }
        return True
    
    def send_message(self, from_user_id, to_user_id, content):
        """Send a message from one user to another."""
        if from_user_id not in self.users or to_user_id not in self.users:
            return False
        
        message = {
            'message_id': str(self.message_id_counter),
            'from_user_id': from_user_id,
            'to_user_id': to_user_id,
            'content': content,
            'timestamp': time.time()
        }
        
        self.messages[to_user_id].append(message)
        self.message_id_counter += 1
        return True
    
    def get_messages(self, user_id):
        """Get all messages for a user."""
        return self.messages.get(user_id, [])
    
    def get_message_count(self, user_id):
        """Count messages for a user."""
        return len(self.messages.get(user_id, []))
    
    def get_user(self, user_id):
        """Get user information."""
        return self.users.get(user_id)
    
    def list_all_users(self):
        """Get all registered users."""
        return list(self.users.values())
