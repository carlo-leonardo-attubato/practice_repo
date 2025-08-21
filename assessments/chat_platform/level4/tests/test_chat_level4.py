import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from chat_platform.level4.model_solution.chat import ChatPlatform

class TestChatLevel4:
    def test_video_calls(self):
        chat = ChatPlatform()
        chat.create_user("user1")
        chat.create_user("user2")
        
        # Test video call initiation
        call_id = chat.start_video_call("user1", "user2")
        assert call_id is not None
        
        # Test call status
        status = chat.get_call_status(call_id)
        assert status in ["ringing", "connected", "ended"]
        
        # Test call acceptance
        chat.accept_call("user2", call_id)
        assert chat.get_call_status(call_id) == "connected"
        
    def test_voice_messages(self):
        chat = ChatPlatform()
        chat.create_user("user1")
        chat.create_user("user2")
        
        # Test voice message
        msg_id = chat.send_voice_message("user1", "user2", "voice_data", 30)
        assert msg_id is not None
        
        # Test voice message retrieval
        voice_msg = chat.get_voice_message(msg_id)
        assert voice_msg["duration"] == 30
        assert voice_msg["sender"] == "user1"
        
    def test_chat_analytics(self):
        chat = ChatPlatform()
        chat.create_user("user1")
        chat.create_room("room1")
        chat.join_room("user1", "room1")
        
        # Send some messages
        chat.send_message("user1", "room1", "Hello")
        chat.send_message("user1", "room1", "World")
        
        # Test analytics
        analytics = chat.get_chat_analytics("room1")
        assert analytics["total_messages"] >= 2
        assert analytics["active_users"] >= 1
        
    def test_premium_features(self):
        chat = ChatPlatform()
        chat.create_user("premium_user", is_premium=True)
        chat.create_user("regular_user", is_premium=False)
        
        # Test premium features
        assert chat.has_premium_features("premium_user") == True
        assert chat.has_premium_features("regular_user") == False
        
        # Test premium message length
        long_message = "A" * 1000
        result = chat.send_message("premium_user", "room1", long_message)
        assert result == True  # Premium users can send long messages
