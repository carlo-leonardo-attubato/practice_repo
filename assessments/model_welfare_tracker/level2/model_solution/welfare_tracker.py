"""
LEVEL 2: Interaction Analysis & Filtering - MODEL SOLUTION
Enhanced welfare tracking with analysis capabilities.
"""

import time
from collections import defaultdict


class ModelWelfareTracker:
    """Enhanced AI model welfare tracking with analysis capabilities."""
    
    def __init__(self):
        """Initialize the welfare tracker."""
        self.models = {}  # model_id -> model_data
        self.interactions = defaultdict(list)  # model_id -> list of interactions
    
    # =================== LEVEL 1 METHODS ===================
    
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
    
    # =================== LEVEL 2 NEW METHODS ===================
    
    def get_interactions_in_timerange(self, model_id, start_time, end_time):
        """Get interactions for a model within a time range."""
        interactions = self.interactions.get(model_id, [])
        return [i for i in interactions if start_time <= i['timestamp'] <= end_time]
    
    def get_user_interactions(self, user_id):
        """Get all interactions for a specific user across all models."""
        all_interactions = []
        for model_interactions in self.interactions.values():
            all_interactions.extend([i for i in model_interactions if i['user_id'] == user_id])
        
        return sorted(all_interactions, key=lambda x: x['timestamp'])
    
    def get_interaction_frequency(self, model_id, time_window=3600):
        """Calculate interaction frequency (interactions per hour)."""
        current_time = time.time()
        recent_interactions = self.get_interactions_in_timerange(
            model_id, current_time - time_window, current_time
        )
        
        return len(recent_interactions) / (time_window / 3600)
    
    def get_unique_users(self, model_id):
        """Get unique users who have interacted with a model."""
        interactions = self.interactions.get(model_id, [])
        unique_users = list(set(i['user_id'] for i in interactions))
        return sorted(unique_users)
    
    def get_model_usage_stats(self, model_id):
        """Get comprehensive usage statistics for a model."""
        if model_id not in self.models:
            return None
        
        interactions = self.interactions.get(model_id, [])
        
        if not interactions:
            return {
                'model_id': model_id,
                'total_interactions': 0,
                'unique_users': 0,
                'interactions_per_hour': 0.0,
                'first_interaction': None,
                'last_interaction': None
            }
        
        timestamps = [i['timestamp'] for i in interactions]
        unique_users = self.get_unique_users(model_id)
        
        return {
            'model_id': model_id,
            'total_interactions': len(interactions),
            'unique_users': len(unique_users),
            'interactions_per_hour': self.get_interaction_frequency(model_id),
            'first_interaction': min(timestamps),
            'last_interaction': max(timestamps),
            'average_interactions_per_user': len(interactions) / len(unique_users) if unique_users else 0
        }


if __name__ == "__main__":
    tracker = ModelWelfareTracker()
    
    # Test Level 2 functionality
    print("Testing Level 2 functionality...")
    
    # Register models
    tracker.register_model("claude-3", "Claude 3", "language")
    tracker.register_model("gpt-4", "GPT-4", "language")
    
    # Log interactions
    current_time = time.time()
    for i in range(10):
        tracker.log_interaction("claude-3", f"user{i%3}", current_time + i*60)
    
    # Test time range filtering
    recent = tracker.get_interactions_in_timerange("claude-3", current_time, current_time + 300)
    print(f"Recent interactions: {len(recent)}")
    
    # Test user interactions
    user_interactions = tracker.get_user_interactions("user1")
    print(f"User1 interactions: {len(user_interactions)}")
    
    # Test frequency
    frequency = tracker.get_interaction_frequency("claude-3", 3600)
    print(f"Interaction frequency: {frequency:.2f}/hour")
    
    # Test usage stats
    stats = tracker.get_model_usage_stats("claude-3")
    print(f"Usage stats: {stats}")
    
    print("✅ Level 2 implementation complete!")
