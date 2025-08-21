import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from assessments.task_queue.level4.model_solution.task_queue import TaskQueue

class TestTaskQueueLevel4:
    def test_distributed_task_processing(self):
        queue = TaskQueue()
        
        # Test worker registration
        worker_id = queue.register_worker("worker1")
        assert worker_id is not None
        
        # Test task assignment to worker
        task_id = queue.add_task("distributed_task")
        assigned_worker = queue.assign_task_to_worker(task_id, worker_id)
        assert assigned_worker == worker_id
        
    def test_task_load_balancing(self):
        queue = TaskQueue()
        
        # Register multiple workers
        worker1 = queue.register_worker("worker1")
        worker2 = queue.register_worker("worker2")
        
        # Add tasks
        for i in range(10):
            queue.add_task(f"task{i}")
        
        # Test load balancing
        assignments = queue.get_worker_assignments()
        assert len(assignments[worker1]) >= 4  # Roughly balanced
        assert len(assignments[worker2]) >= 4
        
    def test_task_monitoring(self):
        queue = TaskQueue()
        
        # Add tasks and monitor
        task_id = queue.add_task("monitored_task")
        
        # Test monitoring
        status = queue.get_task_status(task_id)
        assert status in ["pending", "running", "completed", "failed"]
        
        # Test performance metrics
        metrics = queue.get_performance_metrics()
        assert "average_execution_time" in metrics
        assert "throughput" in metrics
        
    def test_advanced_scheduling(self):
        queue = TaskQueue()
        
        # Test cron-like scheduling
        task_id = queue.add_task("cron_task", cron_schedule="0 0 * * *")
        
        # Test schedule parsing
        schedule = queue.get_task_schedule(task_id)
        assert schedule["type"] == "cron"
        assert schedule["expression"] == "0 0 * * *"
        
        # Test next execution time
        next_run = queue.get_next_execution_time(task_id)
        assert next_run > 0
