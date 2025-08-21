import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from assessments.task_queue.level3.model_solution.task_queue import TaskQueue

class TestTaskQueueLevel3:
    def test_task_retry_mechanism(self):
        queue = TaskQueue()
        task_id = queue.add_task("retry_task", max_retries=3)
        
        # Test retry logic
        assert queue.get_retry_count(task_id) == 0
        
        # Simulate task failure
        queue.fail_task(task_id)
        assert queue.get_retry_count(task_id) == 1
        assert queue.can_retry(task_id) == True
        
        # Test max retries
        for _ in range(3):
            queue.fail_task(task_id)
        
        assert queue.can_retry(task_id) == False
        
    def test_task_scheduling(self):
        queue = TaskQueue()
        
        # Add scheduled task
        task_id = queue.add_task("scheduled_task", schedule_time=1000)
        
        # Test scheduling
        assert queue.is_task_scheduled(task_id) == True
        assert queue.get_schedule_time(task_id) == 1000
        
    def test_task_batching(self):
        queue = TaskQueue()
        
        # Add batch of tasks
        batch_id = queue.create_batch("batch1")
        task1 = queue.add_task("task1", batch_id=batch_id)
        task2 = queue.add_task("task2", batch_id=batch_id)
        
        # Test batch operations
        batch_tasks = queue.get_batch_tasks(batch_id)
        assert len(batch_tasks) == 2
        
        # Test batch completion
        queue.complete_batch(batch_id)
        assert queue.is_batch_complete(batch_id) == True
        
    def test_task_metrics(self):
        queue = TaskQueue()
        
        # Add and complete some tasks
        task1 = queue.add_task("task1")
        task2 = queue.add_task("task2")
        queue.complete_task(task1)
        queue.fail_task(task2)
        
        # Test metrics
        metrics = queue.get_queue_metrics()
        assert metrics["total_tasks"] >= 2
        assert metrics["completed_tasks"] >= 1
        assert metrics["failed_tasks"] >= 1
