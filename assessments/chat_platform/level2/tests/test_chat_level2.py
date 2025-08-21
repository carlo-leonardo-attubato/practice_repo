import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from chat_platform.level2.model_solution.chat import ChatPlatform

class TestChatLevel2:
    def test_private_messaging(self):
        chat = ChatPlatform()
        chat.create_user("alice")
        chat.create_user("bob")
        
        # Test private message
        result = chat.send_private_message("alice", "bob", "Hello Bob!")
        assert result == True
        
        # Test get private messages
        messages = chat.get_private_messages("alice", "bob")
        assert len(messages) == 1
        assert messages[0]["content"] == "Hello Bob!"
        
    def test_user_status(self):
        chat = ChatPlatform()
        chat.create_user("user1")
        
        # Test status updates
        chat.set_user_status("user1", "online")
        assert chat.get_user_status("user1") == "online"
        
        chat.set_user_status("user1", "away")
        assert chat.get_user_status("user1") == "away"
        
    def test_message_editing(self):
        chat = ChatPlatform()
        chat.create_user("user1")
        chat.create_room("room1")
        chat.join_room("user1", "room1")
        
        # Send message
        msg_id = chat.send_message("user1", "room1", "Hello world!")
        assert msg_id is not None
        
        # Edit message
        result = chat.edit_message("user1", msg_id, "Hello updated world!")
        assert result == True
        
        # Verify edit
        messages = chat.get_room_messages("room1")
        edited_msg = next((msg for msg in messages if msg["id"] == msg_id), None)
        assert edited_msg["content"] == "Hello updated world!"
        
    def test_user_typing_indicator(self):
        chat = ChatPlatform()
        chat.create_user("user1")
        chat.create_room("room1")
        chat.join_room("user1", "room1")
        
        # Test typing indicator
        chat.set_typing("user1", "room1", True)
        assert chat.is_typing("user1", "room1") == True
        
        chat.set_typing("user1", "room1", False)
        assert chat.is_typing("user1", "room1") == False
