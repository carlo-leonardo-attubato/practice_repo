"""
LEVEL 2: Interaction Analysis & Filtering
Build on Level 1 by adding interaction analysis and filtering capabilities.

Time Limit: 20-25 minutes
Points: ~150 points

New Requirements (in addition to Level 1):
- Filter interactions by time range
- Search interactions by user
- Calculate interaction frequencies
- Basic welfare metrics and analysis
"""

import time
from collections import defaultdict


class ModelWelfareTracker:
    """
    Enhanced AI model welfare tracking with analysis capabilities.
    
    IMPLEMENT ALL LEVEL 1 METHODS PLUS:
    - get_interactions_in_timerange(self, model_id, start_time, end_time): Filter by time
    - get_user_interactions(self, user_id): Get all interactions for a user
    - get_interaction_frequency(self, model_id, time_window): Calculate frequency
    - get_unique_users(self, model_id): Get unique users for a model
    - get_model_usage_stats(self, model_id): Get comprehensive usage statistics
    """
    
    def __init__(self):
        """Initialize the welfare tracker."""
        # TODO: Initialize storage for models and interactions
        pass
    
    # =================== LEVEL 1 METHODS ===================
    # Copy your Level 1 implementation here
    
    def register_model(self, model_id, name, model_type):
        """Register a new AI model."""
        # TODO: Copy from Level 1
        pass
    
    def get_model(self, model_id):
        """Retrieve model information."""
        # TODO: Copy from Level 1
        pass
    
    def log_interaction(self, model_id, user_id, timestamp):
        """Log a user interaction with a model."""
        # TODO: Copy from Level 1
        pass
    
    def get_model_interactions(self, model_id):
        """Get all interactions for a specific model."""
        # TODO: Copy from Level 1
        pass
    
    def get_interaction_count(self, model_id):
        """Count total interactions for a model."""
        # TODO: Copy from Level 1
        pass
    
    def list_all_models(self):
        """Get all registered models."""
        # TODO: Copy from Level 1
        pass
    
    # =================== LEVEL 2 NEW METHODS ===================
    
    def get_interactions_in_timerange(self, model_id, start_time, end_time):
        """
        Get interactions for a model within a time range.
        
        Args:
            model_id (str): Model identifier
            start_time (float): Start timestamp (inclusive)
            end_time (float): End timestamp (inclusive)
            
        Returns:
            list: List of interactions in the time range
        """
        # TODO: Implement time-based filtering
        pass
    
    def get_user_interactions(self, user_id):
        """
        Get all interactions for a specific user across all models.
        
        Args:
            user_id (str): User identifier
            
        Returns:
            list: List of interactions by the user, sorted by timestamp
        """
        # TODO: Implement user interaction retrieval
        pass
    
    def get_interaction_frequency(self, model_id, time_window=3600):
        """
        Calculate interaction frequency (interactions per hour).
        
        Args:
            model_id (str): Model identifier
            time_window (int): Time window in seconds (default: 1 hour)
            
        Returns:
            float: Interactions per hour in the time window
        """
        # TODO: Implement frequency calculation
        pass
    
    def get_unique_users(self, model_id):
        """
        Get unique users who have interacted with a model.
        
        Args:
            model_id (str): Model identifier
            
        Returns:
            list: List of unique user IDs
        """
        # TODO: Implement unique user retrieval
        pass
    
    def get_model_usage_stats(self, model_id):
        """
        Get comprehensive usage statistics for a model.
        
        Args:
            model_id (str): Model identifier
            
        Returns:
            dict: Usage statistics, None if model not found
        """
        # TODO: Implement usage statistics
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    tracker = ModelWelfareTracker()
    print("Level 2: Implement the enhanced ModelWelfareTracker methods!")
