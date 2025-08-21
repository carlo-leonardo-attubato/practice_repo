import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from assessments.task_queue.level2.model_solution.task_queue import TaskQueue

class TestTaskQueueLevel2:
    def test_task_priorities(self):
        queue = TaskQueue()
        
        # Add tasks with different priorities
        queue.add_task("low_task", priority=1)
        queue.add_task("high_task", priority=10)
        queue.add_task("medium_task", priority=5)
        
        # Test priority ordering
        tasks = queue.get_all_tasks()
        assert tasks[0]["priority"] == 10  # Highest priority first
        assert tasks[1]["priority"] == 5
        assert tasks[2]["priority"] == 1
        
    def test_task_categories(self):
        queue = TaskQueue()
        
        # Add tasks with categories
        queue.add_task("email_task", category="communication")
        queue.add_task("backup_task", category="maintenance")
        queue.add_task("report_task", category="reporting")
        
        # Test category filtering
        comm_tasks = queue.get_tasks_by_category("communication")
        assert len(comm_tasks) == 1
        assert comm_tasks[0]["name"] == "email_task"
        
    def test_task_dependencies(self):
        queue = TaskQueue()
        
        # Add tasks with dependencies
        task1_id = queue.add_task("task1")
        task2_id = queue.add_task("task2", dependencies=[task1_id])
        
        # Test dependency checking
        assert queue.can_execute(task2_id) == False  # task1 not completed
        assert queue.can_execute(task1_id) == True   # no dependencies
        
        # Complete dependency
        queue.complete_task(task1_id)
        assert queue.can_execute(task2_id) == True
        
    def test_task_timeout(self):
        queue = TaskQueue()
        
        # Add task with timeout
        task_id = queue.add_task("timeout_task", timeout=60)
        
        # Test timeout checking
        assert queue.is_task_expired(task_id) == False
        
        # Simulate timeout (would need time manipulation in real test)
        # For now, just test the method exists
        assert hasattr(queue, 'is_task_expired')
