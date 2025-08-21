"""
LEVEL 3: Advanced Chat Features & Moderation - MODEL SOLUTION
Complex messaging features with moderation and TTL.
"""

import time
from collections import defaultdict


class ChatPlatform:
    """Advanced chat platform with moderation and TTL messages."""
    
    def __init__(self):
        """Initialize the chat platform."""
        self.users = {}
        self.messages = defaultdict(list)
        self.message_id_counter = 1
        self.blocked_users = defaultdict(set)  # user_id -> set of blocked users
        self.message_edits = defaultdict(list)  # message_id -> edit history
        self.banned_words = set()
    
    # =================== LEVEL 1-2 METHODS ===================
    
    def register_user(self, user_id, username):
        if user_id in self.users:
            return False
        self.users[user_id] = {
            'user_id': user_id, 'username': username, 'registered_at': time.time(),
            'status': 'online'
        }
        return True
    
    def send_message(self, from_user_id, to_user_id, content, ttl_seconds=None):
        if from_user_id not in self.users or to_user_id not in self.users:
            return None
        
        # Check if sender is blocked
        if from_user_id in self.blocked_users[to_user_id]:
            return None
        
        # Content moderation
        if self._is_content_inappropriate(content):
            return None
        
        message_id = str(self.message_id_counter)
        self.message_id_counter += 1
        
        message = {
            'message_id': message_id,
            'from_user_id': from_user_id,
            'to_user_id': to_user_id,
            'content': content,
            'timestamp': time.time(),
            'expires_at': time.time() + ttl_seconds if ttl_seconds else None,
            'edited': False
        }
        
        self.messages[to_user_id].append(message)
        return message_id
    
    def get_messages(self, user_id, include_expired=False):
        messages = self.messages.get(user_id, [])
        if include_expired:
            return messages
        
        # Filter out expired messages
        current_time = time.time()
        valid_messages = []
        for msg in messages:
            if msg['expires_at'] is None or current_time < msg['expires_at']:
                valid_messages.append(msg)
        
        return valid_messages
    
    def get_message_count(self, user_id):
        return len(self.get_messages(user_id))
    
    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def list_all_users(self):
        return list(self.users.values())
    
    def search_messages(self, user_id, query):
        messages = self.get_messages(user_id)
        query_lower = query.lower()
        return [m for m in messages if query_lower in m['content'].lower()]
    
    def get_messages_in_timerange(self, user_id, start_time, end_time):
        messages = self.get_messages(user_id)
        return [m for m in messages if start_time <= m['timestamp'] <= end_time]
    
    def set_user_status(self, user_id, status):
        if user_id not in self.users:
            return False
        self.users[user_id]['status'] = status
        return True
    
    def get_conversation(self, user1_id, user2_id):
        user1_messages = [m for m in self.get_messages(user1_id) if m['from_user_id'] == user2_id]
        user2_messages = [m for m in self.get_messages(user2_id) if m['from_user_id'] == user1_id]
        all_messages = user1_messages + user2_messages
        return sorted(all_messages, key=lambda x: x['timestamp'])
    
    # =================== LEVEL 3 NEW METHODS ===================
    
    def edit_message(self, message_id, new_content, editor_user_id):
        """Edit a message and track history."""
        # Find the message
        for user_messages in self.messages.values():
            for message in user_messages:
                if message['message_id'] == message_id:
                    if message['from_user_id'] != editor_user_id:
                        return False  # Can only edit own messages
                    
                    # Content moderation
                    if self._is_content_inappropriate(new_content):
                        return False
                    
                    # Save edit history
                    self.message_edits[message_id].append({
                        'old_content': message['content'],
                        'new_content': new_content,
                        'edited_at': time.time(),
                        'editor_id': editor_user_id
                    })
                    
                    message['content'] = new_content
                    message['edited'] = True
                    return True
        
        return False
    
    def delete_message(self, message_id, deleter_user_id):
        """Delete a message."""
        for user_id, user_messages in self.messages.items():
            for i, message in enumerate(user_messages):
                if message['message_id'] == message_id:
                    if message['from_user_id'] != deleter_user_id:
                        return False
                    
                    # Mark as deleted instead of removing
                    message['content'] = "[Message deleted]"
                    message['deleted'] = True
                    message['deleted_at'] = time.time()
                    return True
        
        return False
    
    def block_user(self, blocker_user_id, blocked_user_id):
        """Block a user from sending messages."""
        if blocker_user_id not in self.users or blocked_user_id not in self.users:
            return False
        
        self.blocked_users[blocker_user_id].add(blocked_user_id)
        return True
    
    def unblock_user(self, blocker_user_id, blocked_user_id):
        """Unblock a user."""
        if blocker_user_id not in self.users:
            return False
        
        self.blocked_users[blocker_user_id].discard(blocked_user_id)
        return True
    
    def add_banned_word(self, word):
        """Add word to content moderation list."""
        self.banned_words.add(word.lower())
        return True
    
    def cleanup_expired_messages(self):
        """Remove expired messages."""
        current_time = time.time()
        total_removed = 0
        
        for user_id in self.messages:
            original_count = len(self.messages[user_id])
            self.messages[user_id] = [
                msg for msg in self.messages[user_id]
                if msg['expires_at'] is None or current_time < msg['expires_at']
            ]
            total_removed += original_count - len(self.messages[user_id])
        
        return total_removed
    
    def _is_content_inappropriate(self, content):
        """Check if content contains banned words."""
        content_lower = content.lower()
        return any(banned_word in content_lower for banned_word in self.banned_words)
    
    def get_message_edit_history(self, message_id):
        """Get edit history for a message."""
        return self.message_edits.get(message_id, [])


# Quick test - uncomment when ready
if __name__ == "__main__":
    chat = ChatPlatform()
    print("Level 3: Implement the advanced chat features!")
