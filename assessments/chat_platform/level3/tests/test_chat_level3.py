import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from chat_platform.level3.model_solution.chat import ChatPlatform

class TestChatLevel3:
    def test_file_sharing(self):
        chat = ChatPlatform()
        chat.create_user("user1")
        chat.create_room("room1")
        chat.join_room("user1", "room1")
        
        # Test file upload
        file_id = chat.upload_file("user1", "room1", "document.pdf", "pdf", 1024)
        assert file_id is not None
        
        # Test file download
        file_info = chat.get_file_info(file_id)
        assert file_info["name"] == "document.pdf"
        assert file_info["type"] == "pdf"
        
    def test_message_reactions(self):
        chat = ChatPlatform()
        chat.create_user("user1")
        chat.create_room("room1")
        chat.join_room("user1", "room1")
        
        # Send message
        msg_id = chat.send_message("user1", "room1", "Hello!")
        
        # Add reaction
        chat.add_reaction("user1", msg_id, "👍")
        reactions = chat.get_message_reactions(msg_id)
        assert "👍" in reactions
        
    def test_user_roles(self):
        chat = ChatPlatform()
        chat.create_user("admin")
        chat.create_user("moderator")
        chat.create_user("user")
        chat.create_room("room1")
        
        # Test role assignment
        chat.set_user_role("admin", "room1", "admin")
        chat.set_user_role("moderator", "room1", "moderator")
        
        assert chat.get_user_role("admin", "room1") == "admin"
        assert chat.get_user_role("moderator", "room1") == "moderator"
        assert chat.get_user_role("user", "room1") == "user"
        
    def test_message_moderation(self):
        chat = ChatPlatform()
        chat.create_user("moderator")
        chat.create_user("user1")
        chat.create_room("room1")
        chat.join_room("moderator", "room1")
        chat.join_room("user1", "room1")
        chat.set_user_role("moderator", "room1", "moderator")
        
        # Send message
        msg_id = chat.send_message("user1", "room1", "Hello!")
        
        # Test moderation
        chat.flag_message(msg_id, "inappropriate")
        assert chat.is_message_flagged(msg_id) == True
        
        # Test message removal
        chat.remove_message("moderator", msg_id)
        messages = chat.get_room_messages("room1")
        assert len(messages) == 0
