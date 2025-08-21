"""
Unit Tests for Level 1: Basic Model Registration & Interaction Logging
"""

import pytest
import sys
import os
import time

# Add the candidate directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'candidate'))

from welfare_tracker import ModelWelfareTracker


class TestModelWelfareTrackerLevel1:
    """Test cases for Level 1 ModelWelfareTracker."""
    
    def setup_method(self):
        """Set up a fresh ModelWelfareTracker instance before each test."""
        self.tracker = ModelWelfareTracker()
    
    def test_initialization(self):
        """Test that ModelWelfareTracker initializes correctly."""
        assert self.tracker is not None
        assert hasattr(self.tracker, 'models')
        assert hasattr(self.tracker, 'interactions')
    
    def test_register_model_basic(self):
        """Test basic model registration."""
        result = self.tracker.register_model("claude-3", "Claude 3", "language")
        assert result is True
        
        model = self.tracker.get_model("claude-3")
        assert model is not None
        assert model['id'] == "claude-3"
        assert model['name'] == "Claude 3"
        assert model['type'] == "language"
    
    def test_register_model_duplicate(self):
        """Test registering model with duplicate ID."""
        self.tracker.register_model("claude-3", "Claude 3", "language")
        result = self.tracker.register_model("claude-3", "Different Claude", "vision")
        assert result is False
    
    def test_register_multiple_models(self):
        """Test registering multiple models."""
        self.tracker.register_model("claude-3", "Claude 3", "language")
        self.tracker.register_model("gpt-4", "GPT-4", "language")
        self.tracker.register_model("dalle-3", "DALL-E 3", "vision")
        
        models = self.tracker.list_all_models()
        assert len(models) == 3
        
        model_ids = [m['id'] for m in models]
        assert "claude-3" in model_ids
        assert "gpt-4" in model_ids
        assert "dalle-3" in model_ids
    
    def test_get_model_nonexistent(self):
        """Test getting non-existent model."""
        model = self.tracker.get_model("nonexistent")
        assert model is None
    
    def test_log_interaction_valid(self):
        """Test logging interaction for existing model."""
        self.tracker.register_model("claude-3", "Claude 3", "language")
        
        current_time = time.time()
        result = self.tracker.log_interaction("claude-3", "user1", current_time)
        assert result is True
        
        interactions = self.tracker.get_model_interactions("claude-3")
        assert len(interactions) == 1
        assert interactions[0]['user_id'] == "user1"
        assert interactions[0]['timestamp'] == current_time
    
    def test_log_interaction_nonexistent_model(self):
        """Test logging interaction for non-existent model."""
        result = self.tracker.log_interaction("nonexistent", "user1", time.time())
        assert result is False
    
    def test_get_interaction_count(self):
        """Test interaction counting."""
        self.tracker.register_model("claude-3", "Claude 3", "language")
        
        assert self.tracker.get_interaction_count("claude-3") == 0
        
        current_time = time.time()
        self.tracker.log_interaction("claude-3", "user1", current_time)
        self.tracker.log_interaction("claude-3", "user2", current_time + 1)
        
        assert self.tracker.get_interaction_count("claude-3") == 2
    
    def test_get_interaction_count_nonexistent(self):
        """Test interaction count for non-existent model."""
        count = self.tracker.get_interaction_count("nonexistent")
        assert count == 0
    
    def test_get_model_interactions_empty(self):
        """Test getting interactions for model with no interactions."""
        self.tracker.register_model("claude-3", "Claude 3", "language")
        interactions = self.tracker.get_model_interactions("claude-3")
        assert interactions == []
    
    def test_get_model_interactions_nonexistent(self):
        """Test getting interactions for non-existent model."""
        interactions = self.tracker.get_model_interactions("nonexistent")
        assert interactions == []
    
    def test_list_all_models_empty(self):
        """Test listing models when none registered."""
        models = self.tracker.list_all_models()
        assert models == []
    
    def test_comprehensive_workflow(self):
        """Test complete Level 1 workflow."""
        # Register models
        self.tracker.register_model("claude-3", "Claude 3", "language")
        self.tracker.register_model("dalle-3", "DALL-E 3", "vision")
        
        # Log interactions
        current_time = time.time()
        self.tracker.log_interaction("claude-3", "user1", current_time)
        self.tracker.log_interaction("claude-3", "user2", current_time + 1)
        self.tracker.log_interaction("dalle-3", "user1", current_time + 2)
        
        # Verify counts
        assert self.tracker.get_interaction_count("claude-3") == 2
        assert self.tracker.get_interaction_count("dalle-3") == 1
        
        # Verify model listing
        models = self.tracker.list_all_models()
        assert len(models) == 2
        
        # Verify interactions
        claude_interactions = self.tracker.get_model_interactions("claude-3")
        assert len(claude_interactions) == 2
        assert claude_interactions[0]['user_id'] == "user1"
        assert claude_interactions[1]['user_id'] == "user2"


def run_tests():
    """Run all tests and display results."""
    print("🧪 Level 1: Basic Model Registration & Interaction Logging")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ Level 1 tests completed!")


if __name__ == "__main__":
    run_tests()
