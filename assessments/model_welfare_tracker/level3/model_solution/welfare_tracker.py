"""
LEVEL 3: Welfare Monitoring & Rate Limiting - MODEL SOLUTION
Complex welfare tracking and protection mechanisms.
"""

import time
from collections import defaultdict


class ModelWelfareTracker:
    """Advanced AI model welfare tracking with rate limiting."""
    
    def __init__(self):
        """Initialize the welfare tracker."""
        self.models = {}
        self.interactions = defaultdict(list)
        self.rate_limits = {}  # (model_id, user_id) -> limit_data
        self.cooldowns = {}  # model_id -> cooldown_end_time
    
    # =================== LEVEL 1-2 METHODS ===================
    
    def register_model(self, model_id, name, model_type):
        if model_id in self.models:
            return False
        self.models[model_id] = {
            'id': model_id, 'name': name, 'type': model_type,
            'registered_at': time.time()
        }
        return True
    
    def get_model(self, model_id):
        return self.models.get(model_id)
    
    def log_interaction(self, model_id, user_id, timestamp):
        if model_id not in self.models:
            return False
        self.interactions[model_id].append({
            'user_id': user_id, 'timestamp': timestamp, 'model_id': model_id
        })
        return True
    
    def get_model_interactions(self, model_id):
        return self.interactions.get(model_id, [])
    
    def get_interaction_count(self, model_id):
        return len(self.interactions.get(model_id, []))
    
    def list_all_models(self):
        return list(self.models.values())
    
    def get_interactions_in_timerange(self, model_id, start_time, end_time):
        interactions = self.interactions.get(model_id, [])
        return [i for i in interactions if start_time <= i['timestamp'] <= end_time]
    
    def get_user_interactions(self, user_id):
        all_interactions = []
        for model_interactions in self.interactions.values():
            all_interactions.extend([i for i in model_interactions if i['user_id'] == user_id])
        return sorted(all_interactions, key=lambda x: x['timestamp'])
    
    def get_interaction_frequency(self, model_id, time_window=3600):
        current_time = time.time()
        recent_interactions = self.get_interactions_in_timerange(
            model_id, current_time - time_window, current_time
        )
        return len(recent_interactions) / (time_window / 3600)
    
    # =================== LEVEL 3 NEW METHODS ===================
    
    def calculate_stress_score(self, model_id, time_window=3600):
        """Calculate model stress score based on interaction patterns."""
        if model_id not in self.models:
            return 0.0
        
        current_time = time.time()
        recent_interactions = self.get_interactions_in_timerange(
            model_id, current_time - time_window, current_time
        )
        
        if not recent_interactions:
            return 0.0
        
        # Calculate stress factors
        interaction_rate = len(recent_interactions) / (time_window / 3600)
        unique_users = len(set(i['user_id'] for i in recent_interactions))
        
        # Stress increases with high interaction rate and low user diversity
        base_stress = min(interaction_rate / 10.0, 1.0)  # Cap at 1.0
        diversity_factor = max(0.1, 1.0 / unique_users) if unique_users > 0 else 1.0
        
        return min(base_stress * diversity_factor, 1.0)
    
    def set_rate_limit(self, model_id, user_id, max_interactions, time_window):
        """Set rate limit for user-model pair."""
        if model_id not in self.models:
            return False
        
        self.rate_limits[(model_id, user_id)] = {
            'max_interactions': max_interactions,
            'time_window': time_window,
            'set_at': time.time()
        }
        return True
    
    def check_rate_limit(self, model_id, user_id):
        """Check if user has exceeded rate limit for model."""
        limit_key = (model_id, user_id)
        if limit_key not in self.rate_limits:
            return True  # No limit set
        
        limit_data = self.rate_limits[limit_key]
        current_time = time.time()
        window_start = current_time - limit_data['time_window']
        
        # Count recent interactions
        recent_interactions = [
            i for i in self.interactions.get(model_id, [])
            if i['user_id'] == user_id and i['timestamp'] >= window_start
        ]
        
        return len(recent_interactions) < limit_data['max_interactions']
    
    def enforce_cooldown(self, model_id, cooldown_seconds):
        """Enforce cooldown period for a model."""
        if model_id not in self.models:
            return False
        
        self.cooldowns[model_id] = time.time() + cooldown_seconds
        return True
    
    def is_model_in_cooldown(self, model_id):
        """Check if model is currently in cooldown."""
        if model_id not in self.cooldowns:
            return False
        
        return time.time() < self.cooldowns[model_id]
    
    def get_stressed_models(self, threshold=0.7, time_window=3600):
        """Get models with stress score above threshold."""
        stressed_models = []
        
        for model_id in self.models:
            stress_score = self.calculate_stress_score(model_id, time_window)
            if stress_score >= threshold:
                model_data = self.models[model_id].copy()
                model_data['stress_score'] = stress_score
                stressed_models.append(model_data)
        
        return sorted(stressed_models, key=lambda x: x['stress_score'], reverse=True)
    
    def get_welfare_report(self, model_id):
        """Get comprehensive welfare report for a model."""
        if model_id not in self.models:
            return None
        
        current_time = time.time()
        hour_window = 3600
        day_window = 86400
        
        return {
            'model_id': model_id,
            'model_name': self.models[model_id]['name'],
            'stress_score_1h': self.calculate_stress_score(model_id, hour_window),
            'stress_score_24h': self.calculate_stress_score(model_id, day_window),
            'interactions_1h': len(self.get_interactions_in_timerange(
                model_id, current_time - hour_window, current_time
            )),
            'interactions_24h': len(self.get_interactions_in_timerange(
                model_id, current_time - day_window, current_time
            )),
            'total_interactions': self.get_interaction_count(model_id),
            'in_cooldown': self.is_model_in_cooldown(model_id),
            'cooldown_ends': self.cooldowns.get(model_id, 0)
        }


if __name__ == "__main__":
    tracker = ModelWelfareTracker()
    
    # Test Level 3 functionality
    print("Testing Level 3 welfare monitoring...")
    
    # Register models
    tracker.register_model("claude-3", "Claude 3", "language")
    tracker.register_model("gpt-4", "GPT-4", "language")
    
    # Simulate high usage
    current_time = time.time()
    for i in range(20):
        tracker.log_interaction("claude-3", f"user{i%3}", current_time + i)
    
    # Test stress calculation
    stress = tracker.calculate_stress_score("claude-3")
    print(f"Claude stress score: {stress:.2f}")
    
    # Test rate limiting
    tracker.set_rate_limit("claude-3", "user1", 5, 3600)
    can_interact = tracker.check_rate_limit("claude-3", "user1")
    print(f"User1 can interact with Claude: {can_interact}")
    
    # Test cooldown
    tracker.enforce_cooldown("claude-3", 1800)  # 30 minutes
    in_cooldown = tracker.is_model_in_cooldown("claude-3")
    print(f"Claude in cooldown: {in_cooldown}")
    
    # Test stressed models
    stressed = tracker.get_stressed_models(0.5)
    print(f"Stressed models: {len(stressed)}")
    
    # Test welfare report
    report = tracker.get_welfare_report("claude-3")
    print(f"Welfare report: {report}")
    
    print("✅ Level 3 implementation complete!")
