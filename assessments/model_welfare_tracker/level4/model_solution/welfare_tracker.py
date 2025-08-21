"""
LEVEL 4: Advanced Monitoring & System Management - MODEL SOLUTION
Complete welfare tracking with advanced monitoring.
"""

import time
import copy
from collections import defaultdict


class ModelWelfareTracker:
    """Complete AI model welfare tracking with advanced monitoring."""
    
    def __init__(self):
        """Initialize the welfare tracker."""
        self.models = {}
        self.interactions = defaultdict(list)
        self.rate_limits = {}  # (model_id, user_id) -> limit_data
        self.cooldowns = {}  # model_id -> cooldown_end_time
        self.model_versions = defaultdict(list)  # model_id -> list of versions
        self.system_backups = {}  # backup_id -> complete state
    
    # =================== LEVEL 1-3 METHODS ===================
    # (Complete implementation from previous levels)
    
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
    
    def get_unique_users(self, model_id):
        interactions = self.interactions.get(model_id, [])
        return sorted(list(set(i['user_id'] for i in interactions)))
    
    def get_model_usage_stats(self, model_id):
        if model_id not in self.models:
            return None
        interactions = self.interactions.get(model_id, [])
        if not interactions:
            return {
                'model_id': model_id, 'total_interactions': 0, 'unique_users': 0,
                'interactions_per_hour': 0.0, 'first_interaction': None, 'last_interaction': None
            }
        timestamps = [i['timestamp'] for i in interactions]
        unique_users = self.get_unique_users(model_id)
        return {
            'model_id': model_id, 'total_interactions': len(interactions),
            'unique_users': len(unique_users), 'interactions_per_hour': self.get_interaction_frequency(model_id),
            'first_interaction': min(timestamps), 'last_interaction': max(timestamps),
            'average_interactions_per_user': len(interactions) / len(unique_users) if unique_users else 0
        }
    
    def calculate_stress_score(self, model_id, time_window=3600):
        if model_id not in self.models:
            return 0.0
        current_time = time.time()
        recent_interactions = self.get_interactions_in_timerange(
            model_id, current_time - time_window, current_time
        )
        if not recent_interactions:
            return 0.0
        interaction_rate = len(recent_interactions) / (time_window / 3600)
        unique_users = len(set(i['user_id'] for i in recent_interactions))
        base_stress = min(interaction_rate / 10.0, 1.0)
        diversity_factor = max(0.1, 1.0 / unique_users) if unique_users > 0 else 1.0
        return min(base_stress * diversity_factor, 1.0)
    
    def set_rate_limit(self, model_id, user_id, max_interactions, time_window):
        if model_id not in self.models:
            return False
        self.rate_limits[(model_id, user_id)] = {
            'max_interactions': max_interactions, 'time_window': time_window, 'set_at': time.time()
        }
        return True
    
    def check_rate_limit(self, model_id, user_id):
        limit_key = (model_id, user_id)
        if limit_key not in self.rate_limits:
            return True
        limit_data = self.rate_limits[limit_key]
        current_time = time.time()
        window_start = current_time - limit_data['time_window']
        recent_interactions = [
            i for i in self.interactions.get(model_id, [])
            if i['user_id'] == user_id and i['timestamp'] >= window_start
        ]
        return len(recent_interactions) < limit_data['max_interactions']
    
    def enforce_cooldown(self, model_id, cooldown_seconds):
        if model_id not in self.models:
            return False
        self.cooldowns[model_id] = time.time() + cooldown_seconds
        return True
    
    def is_model_in_cooldown(self, model_id):
        if model_id not in self.cooldowns:
            return False
        return time.time() < self.cooldowns[model_id]
    
    def get_stressed_models(self, threshold=0.7, time_window=3600):
        stressed_models = []
        for model_id in self.models:
            stress_score = self.calculate_stress_score(model_id, time_window)
            if stress_score >= threshold:
                model_data = self.models[model_id].copy()
                model_data['stress_score'] = stress_score
                stressed_models.append(model_data)
        return sorted(stressed_models, key=lambda x: x['stress_score'], reverse=True)
    
    def get_welfare_report(self, model_id):
        if model_id not in self.models:
            return None
        current_time = time.time()
        hour_window = 3600
        day_window = 86400
        return {
            'model_id': model_id, 'model_name': self.models[model_id]['name'],
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
    
    # =================== LEVEL 4 NEW METHODS ===================
    
    def register_model_version(self, model_id, version, name, model_type):
        """Register a new version of a model."""
        version_id = f"{model_id}_v{version}"
        
        if version_id in self.models:
            return None
        
        # Register the versioned model
        self.models[version_id] = {
            'id': version_id,
            'base_model_id': model_id,
            'version': version,
            'name': name,
            'type': model_type,
            'registered_at': time.time()
        }
        
        # Track version history
        self.model_versions[model_id].append({
            'version': version,
            'version_id': version_id,
            'registered_at': time.time()
        })
        
        return version_id
    
    def backup_system_state(self, backup_id):
        """Create a complete backup of the system state."""
        self.system_backups[backup_id] = {
            'models': copy.deepcopy(self.models),
            'interactions': copy.deepcopy(dict(self.interactions)),
            'rate_limits': copy.deepcopy(self.rate_limits),
            'cooldowns': copy.deepcopy(self.cooldowns),
            'model_versions': copy.deepcopy(dict(self.model_versions)),
            'backup_timestamp': time.time()
        }
        return True
    
    def restore_system_state(self, backup_id):
        """Restore system from a backup."""
        if backup_id not in self.system_backups:
            return False
        
        backup = self.system_backups[backup_id]
        self.models = copy.deepcopy(backup['models'])
        self.interactions = defaultdict(list, backup['interactions'])
        self.rate_limits = copy.deepcopy(backup['rate_limits'])
        self.cooldowns = copy.deepcopy(backup['cooldowns'])
        self.model_versions = defaultdict(list, backup['model_versions'])
        
        return True
    
    def bulk_log_interactions(self, interactions_list):
        """Log multiple interactions at once."""
        logged_count = 0
        failed_interactions = []
        
        for interaction in interactions_list:
            try:
                result = self.log_interaction(
                    interaction['model_id'],
                    interaction['user_id'],
                    interaction['timestamp']
                )
                if result:
                    logged_count += 1
                else:
                    failed_interactions.append(interaction)
            except (KeyError, TypeError):
                failed_interactions.append(interaction)
        
        return {
            'logged': logged_count,
            'failed': failed_interactions
        }
    
    def get_system_welfare_report(self):
        """Get system-wide welfare analysis."""
        if not self.models:
            return {
                'total_models': 0,
                'total_interactions': 0,
                'stressed_models': [],
                'models_in_cooldown': [],
                'average_stress_score': 0.0
            }
        
        stressed_models = self.get_stressed_models(0.5)
        models_in_cooldown = [model_id for model_id in self.models if self.is_model_in_cooldown(model_id)]
        
        total_interactions = sum(len(interactions) for interactions in self.interactions.values())
        stress_scores = [self.calculate_stress_score(model_id) for model_id in self.models]
        avg_stress = sum(stress_scores) / len(stress_scores) if stress_scores else 0.0
        
        return {
            'total_models': len(self.models),
            'total_interactions': total_interactions,
            'stressed_models': stressed_models,
            'models_in_cooldown': models_in_cooldown,
            'average_stress_score': avg_stress,
            'total_backups': len(self.system_backups),
            'model_types': list(set(m['type'] for m in self.models.values()))
        }
    
    def get_welfare_trends(self, model_id, time_periods):
        """Get historical welfare trends for a model."""
        if model_id not in self.models:
            return []
        
        trends = []
        for period in time_periods:
            start_time = period['start']
            end_time = period['end']
            
            interactions_in_period = self.get_interactions_in_timerange(model_id, start_time, end_time)
            
            if interactions_in_period:
                # Calculate stress for this period
                period_duration = end_time - start_time
                interaction_rate = len(interactions_in_period) / (period_duration / 3600)
                unique_users = len(set(i['user_id'] for i in interactions_in_period))
                
                # Simplified stress calculation for historical data
                stress_score = min(interaction_rate / 10.0, 1.0)
                if unique_users > 0:
                    stress_score *= max(0.1, 1.0 / unique_users)
            else:
                stress_score = 0.0
                interaction_rate = 0.0
                unique_users = 0
            
            trends.append({
                'period_start': start_time,
                'period_end': end_time,
                'interactions': len(interactions_in_period),
                'unique_users': unique_users,
                'interaction_rate': interaction_rate,
                'stress_score': min(stress_score, 1.0)
            })
        
        return trends
    
    def cleanup_old_interactions(self, cutoff_time):
        """Remove interactions older than cutoff time."""
        total_removed = 0
        
        for model_id in list(self.interactions.keys()):
            original_count = len(self.interactions[model_id])
            self.interactions[model_id] = [
                i for i in self.interactions[model_id]
                if i['timestamp'] >= cutoff_time
            ]
            removed_count = original_count - len(self.interactions[model_id])
            total_removed += removed_count
        
        return total_removed


if __name__ == "__main__":
    tracker = ModelWelfareTracker()
    
    # Test Level 4 functionality
    print("Testing Level 4 advanced monitoring...")
    
    # Register models and versions
    tracker.register_model("claude", "Claude", "language")
    claude_v3 = tracker.register_model_version("claude", "3.0", "Claude 3.0", "language")
    print(f"Registered Claude v3.0: {claude_v3}")
    
    # Create system backup
    tracker.backup_system_state("initial")
    print("✅ System backup created")
    
    # Bulk log interactions
    interactions = [
        {'model_id': 'claude', 'user_id': 'user1', 'timestamp': time.time()},
        {'model_id': 'claude', 'user_id': 'user2', 'timestamp': time.time() + 1}
    ]
    bulk_result = tracker.bulk_log_interactions(interactions)
    print(f"Bulk logged: {bulk_result}")
    
    # System welfare report
    system_report = tracker.get_system_welfare_report()
    print(f"System report: {system_report}")
    
    # Welfare trends
    periods = [
        {'start': time.time() - 3600, 'end': time.time()}
    ]
    trends = tracker.get_welfare_trends("claude", periods)
    print(f"Welfare trends: {trends}")
    
    print("✅ Level 4 implementation complete!")
