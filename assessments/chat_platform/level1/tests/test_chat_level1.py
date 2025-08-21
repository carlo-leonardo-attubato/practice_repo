import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from chat_platform.level1.model_solution.chat import ChatPlatform

class TestChatLevel1:
    def test_user_creation(self):
        chat = ChatPlatform()
        
        # Test user creation
        result = chat.create_user("alice")
        assert result == True
        
        # Test duplicate user creation
        result = chat.create_user("alice")
        assert result == False
        
    def test_room_creation(self):
        chat = ChatPlatform()
        chat.create_user("alice")
        
        # Test room creation
        result = chat.create_room("general")
        assert result == True
        
        # Test duplicate room creation
        result = chat.create_room("general")
        assert result == False
        
    def test_join_room(self):
        chat = ChatPlatform()
        chat.create_user("alice")
        chat.create_room("general")
        
        # Test joining room
        result = chat.join_room("alice", "general")
        assert result == True
        
        # Test joining non-existent room
        result = chat.join_room("alice", "nonexistent")
        assert result == False
        
    def test_send_message(self):
        chat = ChatPlatform()
        chat.create_user("alice")
        chat.create_room("general")
        chat.join_room("alice", "general")
        
        # Test sending message
        msg_id = chat.send_message("alice", "general", "Hello world!")
        assert msg_id is not None
        
        # Test sending message to non-existent room
        msg_id = chat.send_message("alice", "nonexistent", "Hello!")
        assert msg_id is None
        
    def test_get_messages(self):
        chat = ChatPlatform()
        chat.create_user("alice")
        chat.create_room("general")
        chat.join_room("alice", "general")
        
        # Send multiple messages
        chat.send_message("alice", "general", "Message 1")
        chat.send_message("alice", "general", "Message 2")
        
        # Test getting messages
        messages = chat.get_room_messages("general")
        assert len(messages) == 2
        assert messages[0]["content"] == "Message 1"
        assert messages[1]["content"] == "Message 2"
