import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from model_welfare_tracker.level2.model_solution.welfare_tracker import ModelWelfareTracker

class TestWelfareTrackerLevel2:
    def test_model_performance_tracking(self):
        tracker = ModelWelfareTracker()
        
        # Add model performance data
        tracker.record_performance("model1", accuracy=0.95, latency=100)
        tracker.record_performance("model1", accuracy=0.92, latency=120)
        
        # Test performance history
        history = tracker.get_performance_history("model1")
        assert len(history) == 2
        assert history[0]["accuracy"] == 0.95
        
    def test_model_comparison(self):
        tracker = ModelWelfareTracker()
        
        # Add multiple models
        tracker.add_model("model1", "classification")
        tracker.add_model("model2", "classification")
        
        tracker.record_performance("model1", accuracy=0.90, latency=100)
        tracker.record_performance("model2", accuracy=0.85, latency=80)
        
        # Test comparison
        comparison = tracker.compare_models("model1", "model2")
        assert comparison["model1"]["accuracy"] > comparison["model2"]["accuracy"]
        assert comparison["model2"]["latency"] < comparison["model1"]["latency"]
        
    def test_alert_system(self):
        tracker = ModelWelfareTracker()
        
        # Set alert thresholds
        tracker.set_alert_threshold("model1", "accuracy", 0.80)
        tracker.set_alert_threshold("model1", "latency", 200)
        
        # Test alert triggering
        tracker.record_performance("model1", accuracy=0.75, latency=250)
        alerts = tracker.get_active_alerts("model1")
        assert len(alerts) >= 2  # Both thresholds exceeded
        
    def test_model_health_score(self):
        tracker = ModelWelfareTracker()
        
        # Add model and record performance
        tracker.add_model("model1", "classification")
        tracker.record_performance("model1", accuracy=0.90, latency=100)
        
        # Test health score calculation
        health_score = tracker.get_model_health_score("model1")
        assert 0 <= health_score <= 100
        assert health_score > 50  # Should be reasonably good
