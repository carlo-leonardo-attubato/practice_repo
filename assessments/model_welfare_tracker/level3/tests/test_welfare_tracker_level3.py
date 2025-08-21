import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from model_welfare_tracker.level3.model_solution.welfare_tracker import ModelWelfareTracker

class TestWelfareTrackerLevel3:
    def test_bias_detection(self):
        tracker = ModelWelfareTracker()
        
        # Add model and record biased predictions
        tracker.add_model("model1", "classification")
        tracker.record_prediction("model1", input_data={"age": 25, "gender": "male"}, prediction=0.8)
        tracker.record_prediction("model1", input_data={"age": 25, "gender": "female"}, prediction=0.3)
        
        # Test bias detection
        bias_report = tracker.detect_bias("model1", "gender")
        assert bias_report["bias_detected"] == True
        assert bias_report["bias_score"] > 0.5
        
    def test_fairness_metrics(self):
        tracker = ModelWelfareTracker()
        
        # Add model and record predictions
        tracker.add_model("model1", "classification")
        for i in range(100):
            tracker.record_prediction("model1", input_data={"group": "A"}, prediction=0.8)
        for i in range(100):
            tracker.record_prediction("model1", input_data={"group": "B"}, prediction=0.4)
        
        # Test fairness metrics
        fairness = tracker.get_fairness_metrics("model1", "group")
        assert "demographic_parity" in fairness
        assert "equalized_odds" in fairness
        
    def test_explanation_generation(self):
        tracker = ModelWelfareTracker()
        
        # Add model and record prediction
        tracker.add_model("model1", "classification")
        tracker.record_prediction("model1", input_data={"feature1": 0.5, "feature2": 0.8}, prediction=0.9)
        
        # Test explanation generation
        explanation = tracker.generate_explanation("model1", {"feature1": 0.5, "feature2": 0.8})
        assert "feature_importance" in explanation
        assert len(explanation["feature_importance"]) > 0
        
    def test_model_interpretability(self):
        tracker = ModelWelfareTracker()
        
        # Add model
        tracker.add_model("model1", "classification")
        
        # Test interpretability metrics
        interpretability = tracker.get_interpretability_score("model1")
        assert 0 <= interpretability <= 1
        
        # Test feature importance
        importance = tracker.get_feature_importance("model1")
        assert len(importance) > 0
