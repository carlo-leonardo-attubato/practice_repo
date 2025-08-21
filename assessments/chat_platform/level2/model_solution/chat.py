"""
LEVEL 2: Enhanced Chat Features - MODEL SOLUTION
Private messaging, user status, message editing, and typing indicators.
"""

import time
import uuid
from collections import defaultdict


class ChatPlatform:
    """Enhanced chat platform with private messaging and user status."""
    
    def __init__(self):
        """Initialize the enhanced chat platform."""
        self.users = {}  # username -> user_data
        self.rooms = {}  # room_name -> room_data
        self.messages = defaultdict(list)  # room_name -> message_list
        self.private_messages = defaultdict(list)  # (user1, user2) -> message_list
        self.user_status = {}  # username -> status
        self.typing_indicators = {}  # (username, room_name) -> timestamp
    
    def create_user(self, username):
        """Create a new user."""
        if username in self.users:
            return False
        
        self.users[username] = {
            'username': username,
            'created_at': time.time()
        }
        self.user_status[username] = 'online'
        return True
    
    def create_room(self, room_name):
        """Create a new chat room."""
        if room_name in self.rooms:
            return False
        
        self.rooms[room_name] = {
            'name': room_name,
            'created_at': time.time(),
            'members': set()
        }
        return True
    
    def join_room(self, username, room_name):
        """Join a chat room."""
        if username not in self.users or room_name not in self.rooms:
            return False
        
        self.rooms[room_name]['members'].add(username)
        return True
    
    def send_message(self, username, room_name, content):
        """Send a message to a room."""
        if username not in self.users or room_name not in self.rooms:
            return None
        
        if username not in self.rooms[room_name]['members']:
            return None
        
        message_id = str(uuid.uuid4())
        message = {
            'id': message_id,
            'username': username,
            'content': content,
            'timestamp': time.time(),
            'edited': False
        }
        
        self.messages[room_name].append(message)
        return message_id
    
    def get_room_messages(self, room_name):
        """Get all messages from a room."""
        return self.messages.get(room_name, [])
    
    def send_private_message(self, from_user, to_user, content):
        """Send a private message to another user."""
        if from_user not in self.users or to_user not in self.users:
            return False
        
        message = {
            'from_user': from_user,
            'to_user': to_user,
            'content': content,
            'timestamp': time.time()
        }
        
        # Store in both directions for easy retrieval
        key1 = tuple(sorted([from_user, to_user]))
        self.private_messages[key1].append(message)
        
        return True
    
    def get_private_messages(self, user1, user2):
        """Get private messages between two users."""
        key = tuple(sorted([user1, user2]))
        return self.private_messages.get(key, [])
    
    def set_user_status(self, username, status):
        """Set user status."""
        if username in self.users:
            self.user_status[username] = status
    
    def get_user_status(self, username):
        """Get user status."""
        return self.user_status.get(username, 'offline')
    
    def edit_message(self, username, message_id, new_content):
        """Edit a message."""
        for room_name, messages in self.messages.items():
            for message in messages:
                if message['id'] == message_id and message['username'] == username:
                    message['content'] = new_content
                    message['edited'] = True
                    return True
        return False
    
    def set_typing(self, username, room_name, is_typing):
        """Set typing indicator for user in room."""
        if is_typing:
            self.typing_indicators[(username, room_name)] = time.time()
        else:
            self.typing_indicators.pop((username, room_name), None)
    
    def is_typing(self, username, room_name):
        """Check if user is typing in room."""
        timestamp = self.typing_indicators.get((username, room_name))
        if timestamp and time.time() - timestamp < 10:  # 10 second timeout
            return True
        return False
