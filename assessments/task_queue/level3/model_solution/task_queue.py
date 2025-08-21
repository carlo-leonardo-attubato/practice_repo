"""
LEVEL 3: Advanced Queue Logic - MODEL SOLUTION
Complex scheduling with dependencies and retry mechanisms.
"""

import time
from collections import deque, defaultdict
import heapq


class TaskQueue:
    """Advanced task queue with dependencies and retry logic."""
    
    def __init__(self):
        """Initialize the task queue."""
        self.tasks = {}  # task_id -> task_data
        self.priority_queue = []  # heap of (priority, timestamp, task_id)
        self.task_id_counter = 1
        self.dependencies = defaultdict(set)  # task_id -> set of prerequisite task_ids
        self.dependents = defaultdict(set)  # task_id -> set of dependent task_ids
        self.workers = {}  # worker_id -> assigned task_id
        self.retry_counts = defaultdict(int)  # task_id -> retry_count
    
    # =================== LEVEL 1-2 METHODS ===================
    
    def add_task(self, title, description, priority=1, dependencies=None, ttl_seconds=None):
        """Add a new task with dependencies and TTL."""
        task_id = str(self.task_id_counter)
        self.task_id_counter += 1
        
        task = {
            'task_id': task_id,
            'title': title,
            'description': description,
            'priority': priority,
            'status': 'pending',
            'created_at': time.time(),
            'completed_at': None,
            'expires_at': time.time() + ttl_seconds if ttl_seconds else None,
            'assigned_worker': None,
            'retry_count': 0
        }
        
        self.tasks[task_id] = task
        
        # Handle dependencies
        if dependencies:
            for dep_task_id in dependencies:
                if dep_task_id in self.tasks:
                    self.dependencies[task_id].add(dep_task_id)
                    self.dependents[dep_task_id].add(task_id)
        
        # Add to queue if no pending dependencies
        if self._can_execute_task(task_id):
            heapq.heappush(self.priority_queue, (-priority, time.time(), task_id))
        
        return task_id
    
    def get_task(self, task_id):
        """Get task information."""
        return self.tasks.get(task_id)
    
    def complete_task(self, task_id):
        """Mark task as completed and unlock dependents."""
        if task_id not in self.tasks:
            return False
        
        task = self.tasks[task_id]
        task['status'] = 'completed'
        task['completed_at'] = time.time()
        
        # Free up worker
        if task['assigned_worker']:
            del self.workers[task['assigned_worker']]
            task['assigned_worker'] = None
        
        # Check if any dependent tasks can now be executed
        for dependent_id in self.dependents[task_id]:
            if self._can_execute_task(dependent_id):
                dependent_task = self.tasks[dependent_id]
                heapq.heappush(self.priority_queue, 
                             (-dependent_task['priority'], time.time(), dependent_id))
        
        return True
    
    def fail_task(self, task_id, max_retries=3):
        """Mark task as failed and potentially retry."""
        if task_id not in self.tasks:
            return False
        
        task = self.tasks[task_id]
        self.retry_counts[task_id] += 1
        
        # Free up worker
        if task['assigned_worker']:
            del self.workers[task['assigned_worker']]
            task['assigned_worker'] = None
        
        if self.retry_counts[task_id] < max_retries:
            # Retry with lower priority
            task['status'] = 'pending'
            task['retry_count'] = self.retry_counts[task_id]
            heapq.heappush(self.priority_queue, 
                         (-task['priority'] + self.retry_counts[task_id], time.time(), task_id))
        else:
            # Max retries reached
            task['status'] = 'failed'
            task['failed_at'] = time.time()
        
        return True
    
    def assign_task_to_worker(self, worker_id):
        """Assign next available task to a worker."""
        while self.priority_queue:
            priority, timestamp, task_id = heapq.heappop(self.priority_queue)
            
            if task_id not in self.tasks:
                continue
            
            task = self.tasks[task_id]
            
            # Check if task is expired
            if task['expires_at'] and time.time() > task['expires_at']:
                task['status'] = 'expired'
                continue
            
            # Check if task can be executed (dependencies met)
            if not self._can_execute_task(task_id):
                continue
            
            # Assign to worker
            task['status'] = 'in_progress'
            task['assigned_worker'] = worker_id
            task['started_at'] = time.time()
            self.workers[worker_id] = task_id
            
            return task
        
        return None
    
    def get_pending_tasks(self):
        """Get all pending tasks."""
        return [task for task in self.tasks.values() if task['status'] == 'pending']
    
    def get_tasks_by_status(self, status):
        """Get tasks by status."""
        return [task for task in self.tasks.values() if task['status'] == status]
    
    def get_task_dependencies(self, task_id):
        """Get dependencies for a task."""
        return list(self.dependencies.get(task_id, set()))
    
    def get_queue_statistics(self):
        """Get comprehensive queue statistics."""
        total_tasks = len(self.tasks)
        status_counts = defaultdict(int)
        
        for task in self.tasks.values():
            status_counts[task['status']] += 1
        
        # Calculate average wait time for completed tasks
        completed_tasks = [t for t in self.tasks.values() if t['status'] == 'completed']
        avg_completion_time = 0.0
        if completed_tasks:
            completion_times = [
                t['completed_at'] - t['created_at'] 
                for t in completed_tasks 
                if t['completed_at']
            ]
            avg_completion_time = sum(completion_times) / len(completion_times) if completion_times else 0.0
        
        return {
            'total_tasks': total_tasks,
            'pending': status_counts['pending'],
            'in_progress': status_counts['in_progress'],
            'completed': status_counts['completed'],
            'failed': status_counts['failed'],
            'expired': status_counts['expired'],
            'active_workers': len(self.workers),
            'queue_length': len(self.priority_queue),
            'average_completion_time': avg_completion_time
        }
    
    def cleanup_expired_tasks(self):
        """Remove expired tasks."""
        current_time = time.time()
        expired_count = 0
        
        for task in self.tasks.values():
            if (task['expires_at'] and 
                current_time > task['expires_at'] and 
                task['status'] not in ['completed', 'failed', 'expired']):
                task['status'] = 'expired'
                expired_count += 1
        
        # Clean up priority queue
        valid_queue = []
        while self.priority_queue:
            priority, timestamp, task_id = heapq.heappop(self.priority_queue)
            if (task_id in self.tasks and 
                self.tasks[task_id]['status'] == 'pending' and
                (not self.tasks[task_id]['expires_at'] or 
                 current_time < self.tasks[task_id]['expires_at'])):
                valid_queue.append((priority, timestamp, task_id))
        
        self.priority_queue = valid_queue
        heapq.heapify(self.priority_queue)
        
        return expired_count
    
    def _can_execute_task(self, task_id):
        """Check if task dependencies are satisfied."""
        dependencies = self.dependencies.get(task_id, set())
        for dep_id in dependencies:
            if dep_id not in self.tasks or self.tasks[dep_id]['status'] != 'completed':
                return False
        return True


if __name__ == "__main__":
    queue = TaskQueue()
    
    # Test Level 3 functionality
    print("Testing Level 3 queue functionality...")
    
    # Add tasks with dependencies
    task1 = queue.add_task("Setup Database", "Initialize DB", priority=5)
    task2 = queue.add_task("Load Data", "Import initial data", priority=3, dependencies=[task1])
    task3 = queue.add_task("Start Server", "Launch web server", priority=1, dependencies=[task1, task2])
    
    print(f"Added tasks: {task1}, {task2}, {task3}")
    
    # Assign tasks to workers
    worker1_task = queue.assign_task_to_worker("worker1")
    print(f"Worker1 assigned: {worker1_task['title'] if worker1_task else 'None'}")
    
    # Complete task and check dependents
    queue.complete_task(task1)
    worker2_task = queue.assign_task_to_worker("worker2")
    print(f"Worker2 assigned: {worker2_task['title'] if worker2_task else 'None'}")
    
    # Get statistics
    stats = queue.get_queue_statistics()
    print(f"Queue stats: {stats}")
    
    print("✅ Level 3 implementation complete!")
