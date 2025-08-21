"""
LEVEL 1: Basic Model Registration & Interaction Logging - MODEL SOLUTION
Core model management and interaction tracking.
"""

import time


class ModelWelfareTracker:
    """Basic AI model welfare tracking system."""
    
    def __init__(self):
        """Initialize the welfare tracker."""
        self.models = {}  # model_id -> model_data
        self.interactions = {}  # model_id -> list of interactions
    
    def register_model(self, model_id, name, model_type):
        """Register a new AI model."""
        if model_id in self.models:
            return False
        
        self.models[model_id] = {
            'id': model_id,
            'name': name,
            'type': model_type,
            'registered_at': time.time()
        }
        
        # Initialize interaction log for this model
        self.interactions[model_id] = []
        
        return True
    
    def get_model(self, model_id):
        """Retrieve model information."""
        return self.models.get(model_id)
    
    def log_interaction(self, model_id, user_id, timestamp):
        """Log a user interaction with a model."""
        if model_id not in self.models:
            return False
        
        interaction = {
            'user_id': user_id,
            'timestamp': timestamp,
            'model_id': model_id
        }
        
        self.interactions[model_id].append(interaction)
        return True
    
    def get_model_interactions(self, model_id):
        """Get all interactions for a specific model."""
        return self.interactions.get(model_id, [])
    
    def get_interaction_count(self, model_id):
        """Count total interactions for a model."""
        return len(self.interactions.get(model_id, []))
    
    def list_all_models(self):
        """Get all registered models."""
        return list(self.models.values())


if __name__ == "__main__":
    tracker = ModelWelfareTracker()
    
    # Test the implementation
    print("Testing Level 1 functionality...")
    
    # Register models
    tracker.register_model("claude-3", "Claude 3", "language")
    tracker.register_model("dalle-3", "DALL-E 3", "vision")
    
    # Log interactions
    current_time = time.time()
    tracker.log_interaction("claude-3", "user1", current_time)
    tracker.log_interaction("claude-3", "user2", current_time + 1)
    tracker.log_interaction("dalle-3", "user1", current_time + 2)
    
    # Test retrieval
    claude_model = tracker.get_model("claude-3")
    print(f"Claude model: {claude_model['name']}")
    
    # Test interaction counting
    claude_interactions = tracker.get_interaction_count("claude-3")
    print(f"Claude interactions: {claude_interactions}")
    
    # Test listing
    all_models = tracker.list_all_models()
    print(f"Total models: {len(all_models)}")
    
    print("✅ Level 1 implementation complete!")
