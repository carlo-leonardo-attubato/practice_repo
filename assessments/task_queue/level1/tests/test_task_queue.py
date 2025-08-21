"""
Unit Tests for Level 1: Basic Task Management
"""

import pytest
import sys
import os
import time

# Add the candidate directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'candidate'))

from task_queue import TaskQueue


class TestTaskQueueLevel1:
    """Test cases for Level 1 TaskQueue."""
    
    def setup_method(self):
        """Set up a fresh TaskQueue instance before each test."""
        self.queue = TaskQueue()
    
    def test_initialization(self):
        """Test that TaskQueue initializes correctly."""
        assert self.queue is not None
        assert self.queue.get_task_count() == 0
        assert self.queue.get_pending_count() == 0
    
    def test_add_task_basic(self):
        """Test basic task addition."""
        task_id = self.queue.add_task("Test Task", "A test task", 1)
        assert task_id is not None
        assert isinstance(task_id, str)
        
        task = self.queue.get_task(task_id)
        assert task is not None
        assert task['title'] == "Test Task"
        assert task['description'] == "A test task"
        assert task['priority'] == 1
        assert task['status'] == 'pending'
    
    def test_add_multiple_tasks(self):
        """Test adding multiple tasks."""
        task1 = self.queue.add_task("Task 1", "First task", 1)
        task2 = self.queue.add_task("Task 2", "Second task", 2)
        task3 = self.queue.add_task("Task 3", "Third task", 3)
        
        assert self.queue.get_task_count() == 3
        assert self.queue.get_pending_count() == 3
        
        # Verify all tasks exist
        assert self.queue.get_task(task1) is not None
        assert self.queue.get_task(task2) is not None
        assert self.queue.get_task(task3) is not None
    
    def test_complete_task_existing(self):
        """Test completing an existing task."""
        task_id = self.queue.add_task("Test Task", "A test task", 1)
        
        result = self.queue.complete_task(task_id)
        assert result is True
        
        task = self.queue.get_task(task_id)
        assert task['status'] == 'completed'
        assert task['completed_at'] is not None
        assert self.queue.get_pending_count() == 0
    
    def test_complete_task_nonexistent(self):
        """Test completing non-existent task."""
        result = self.queue.complete_task("nonexistent")
        assert result is False
    
    def test_get_task_nonexistent(self):
        """Test getting non-existent task."""
        task = self.queue.get_task("nonexistent")
        assert task is None
    
    def test_get_pending_tasks(self):
        """Test getting pending tasks."""
        pending = self.queue.get_pending_tasks()
        assert pending == []
        
        task1 = self.queue.add_task("Task 1", "First task", 1)
        task2 = self.queue.add_task("Task 2", "Second task", 2)
        
        pending = self.queue.get_pending_tasks()
        assert len(pending) == 2
        
        # Complete one task
        self.queue.complete_task(task1)
        pending = self.queue.get_pending_tasks()
        assert len(pending) == 1
        assert pending[0]['task_id'] == task2
    
    def test_get_next_task(self):
        """Test getting next task to process."""
        # No tasks initially
        next_task = self.queue.get_next_task()
        assert next_task is None
        
        # Add tasks with different priorities
        low_priority = self.queue.add_task("Low Priority", "Low", 1)
        high_priority = self.queue.add_task("High Priority", "High", 5)
        medium_priority = self.queue.add_task("Medium Priority", "Medium", 3)
        
        # Should get highest priority first
        next_task = self.queue.get_next_task()
        assert next_task is not None
        assert next_task['priority'] == 5
        assert next_task['title'] == "High Priority"
    
    def test_priority_ordering(self):
        """Test that tasks are processed in priority order."""
        # Add tasks in random priority order
        task1 = self.queue.add_task("Priority 1", "Low", 1)
        task3 = self.queue.add_task("Priority 3", "High", 3)
        task2 = self.queue.add_task("Priority 2", "Medium", 2)
        
        # Should get in order: 3, 2, 1
        next1 = self.queue.get_next_task()
        assert next1['priority'] == 3
        
        next2 = self.queue.get_next_task()
        assert next2['priority'] == 2
        
        next3 = self.queue.get_next_task()
        assert next3['priority'] == 1
        
        # No more tasks
        next4 = self.queue.get_next_task()
        assert next4 is None
    
    def test_comprehensive_workflow(self):
        """Test complete Level 1 workflow."""
        # Add various tasks
        urgent = self.queue.add_task("Urgent Task", "Very important", 10)
        normal = self.queue.add_task("Normal Task", "Regular work", 5)
        low = self.queue.add_task("Low Task", "Can wait", 1)
        
        # Check initial state
        assert self.queue.get_task_count() == 3
        assert self.queue.get_pending_count() == 3
        
        # Process tasks in priority order
        task1 = self.queue.get_next_task()
        assert task1['title'] == "Urgent Task"
        
        task2 = self.queue.get_next_task()
        assert task2['title'] == "Normal Task"
        
        # Complete the urgent task
        self.queue.complete_task(urgent)
        
        # Check pending tasks
        pending = self.queue.get_pending_tasks()
        assert len(pending) == 2  # normal and low (normal was retrieved but not completed)
        
        # Complete remaining tasks
        self.queue.complete_task(normal)
        self.queue.complete_task(low)
        
        # All should be completed
        assert self.queue.get_pending_count() == 0
        
        # Verify completed tasks
        urgent_task = self.queue.get_task(urgent)
        assert urgent_task['status'] == 'completed'


def run_tests():
    """Run all tests and display results."""
    print("🧪 Level 1: Basic Task Management")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ Level 1 tests completed!")


if __name__ == "__main__":
    run_tests()
