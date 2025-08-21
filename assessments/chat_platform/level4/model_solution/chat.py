"""
LEVEL 4: Premium Chat Features - MODEL SOLUTION
Video calls, voice messages, analytics, and premium features.
"""

import time
import uuid
from collections import defaultdict


class ChatPlatform:
    """Premium chat platform with video calls and analytics."""
    
    def __init__(self):
        """Initialize the premium chat platform."""
        self.users = {}  # username -> user_data
        self.rooms = {}  # room_name -> room_data
        self.messages = defaultdict(list)  # room_name -> message_list
        self.video_calls = {}  # call_id -> call_data
        self.voice_messages = {}  # msg_id -> voice_message_data
        self.analytics = defaultdict(dict)  # room_name -> analytics_data
        self.next_call_id = 1001
    
    def create_user(self, username, is_premium=False):
        """Create a new user."""
        if username in self.users:
            return False
        
        self.users[username] = {
            'username': username,
            'is_premium': is_premium,
            'created_at': time.time()
        }
        return True
    
    def create_room(self, room_name):
        """Create a new chat room."""
        if room_name in self.rooms:
            return False
        
        self.rooms[room_name] = {
            'name': room_name,
            'created_at': time.time(),
            'members': set(),
            'message_count': 0
        }
        
        # Initialize analytics
        self.analytics[room_name] = {
            'total_messages': 0,
            'active_users': 0,
            'created_at': time.time()
        }
        
        return True
    
    def join_room(self, username, room_name):
        """Join a chat room."""
        if username not in self.users or room_name not in self.rooms:
            return False
        
        self.rooms[room_name]['members'].add(username)
        self.analytics[room_name]['active_users'] = len(self.rooms[room_name]['members'])
        return True
    
    def send_message(self, username, room_name, content):
        """Send a message to a room."""
        if username not in self.users or room_name not in self.rooms:
            return None
        
        if username not in self.rooms[room_name]['members']:
            return None
        
        # Check message length for non-premium users
        user = self.users[username]
        if not user.get('is_premium', False) and len(content) > 500:
            return None  # Message too long for non-premium users
        
        message_id = str(uuid.uuid4())
        message = {
            'id': message_id,
            'username': username,
            'content': content,
            'timestamp': time.time()
        }
        
        self.messages[room_name].append(message)
        self.rooms[room_name]['message_count'] += 1
        self.analytics[room_name]['total_messages'] += 1
        
        return message_id
    
    def get_room_messages(self, room_name):
        """Get all messages from a room."""
        return self.messages.get(room_name, [])
    
    def start_video_call(self, from_user, to_user):
        """Start a video call."""
        if from_user not in self.users or to_user not in self.users:
            return None
        
        call_id = str(self.next_call_id)
        self.next_call_id += 1
        
        self.video_calls[call_id] = {
            'call_id': call_id,
            'from_user': from_user,
            'to_user': to_user,
            'status': 'ringing',
            'started_at': time.time()
        }
        
        return call_id
    
    def get_call_status(self, call_id):
        """Get video call status."""
        call = self.video_calls.get(call_id)
        return call['status'] if call else None
    
    def accept_call(self, user, call_id):
        """Accept a video call."""
        call = self.video_calls.get(call_id)
        if not call or call['to_user'] != user:
            return False
        
        call['status'] = 'connected'
        call['accepted_at'] = time.time()
        return True
    
    def send_voice_message(self, from_user, to_user, voice_data, duration):
        """Send a voice message."""
        if from_user not in self.users or to_user not in self.users:
            return None
        
        msg_id = str(uuid.uuid4())
        self.voice_messages[msg_id] = {
            'id': msg_id,
            'from_user': from_user,
            'to_user': to_user,
            'voice_data': voice_data,
            'duration': duration,
            'timestamp': time.time()
        }
        
        return msg_id
    
    def get_voice_message(self, msg_id):
        """Get voice message data."""
        return self.voice_messages.get(msg_id)
    
    def get_chat_analytics(self, room_name):
        """Get chat analytics for a room."""
        if room_name not in self.analytics:
            return {}
        
        analytics = self.analytics[room_name].copy()
        analytics['current_time'] = time.time()
        return analytics
    
    def has_premium_features(self, username):
        """Check if user has premium features."""
        user = self.users.get(username)
        return user and user.get('is_premium', False)
