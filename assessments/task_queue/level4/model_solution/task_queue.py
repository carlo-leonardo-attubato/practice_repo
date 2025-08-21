"""
LEVEL 4: Premium Task Queue Features - MODEL SOLUTION
Distributed processing, load balancing, monitoring, and advanced scheduling.
"""

import time
import uuid
from collections import defaultdict, deque


class TaskQueue:
    """Premium task queue with distributed processing and monitoring."""
    
    def __init__(self):
        """Initialize the premium task queue."""
        self.tasks = {}  # task_id -> task_data
        self.priority_queue = deque()  # Priority-based queue
        self.workers = {}  # worker_id -> worker_data
        self.worker_assignments = defaultdict(list)  # worker_id -> [task_ids]
        self.performance_metrics = {
            'total_execution_time': 0,
            'completed_tasks': 0,
            'failed_tasks': 0
        }
        self.next_task_id = 1
        self.next_worker_id = 1001
    
    def add_task(self, name, priority=5, category="default", dependencies=None, timeout=None, cron_schedule=None):
        """Add a new task to the queue."""
        task_id = str(self.next_task_id)
        self.next_task_id += 1
        
        task = {
            'id': task_id,
            'name': name,
            'priority': priority,
            'category': category,
            'status': 'pending',
            'created_at': time.time(),
            'timeout': timeout,
            'retry_count': 0,
            'cron_schedule': cron_schedule,
            'assigned_worker': None
        }
        
        self.tasks[task_id] = task
        
        # Add to priority queue
        self._add_to_priority_queue(task_id)
        
        return task_id
    
    def _add_to_priority_queue(self, task_id):
        """Add task to priority queue maintaining order."""
        task = self.tasks[task_id]
        priority = task['priority']
        
        # Find position to insert based on priority
        insert_pos = 0
        for i, queued_id in enumerate(self.priority_queue):
            if self.tasks[queued_id]['priority'] < priority:
                insert_pos = i
                break
            insert_pos = i + 1
        
        self.priority_queue.insert(insert_pos, task_id)
    
    def register_worker(self, worker_name):
        """Register a new worker."""
        worker_id = str(self.next_worker_id)
        self.next_worker_id += 1
        
        self.workers[worker_id] = {
            'id': worker_id,
            'name': worker_name,
            'status': 'available',
            'registered_at': time.time(),
            'current_task': None
        }
        
        return worker_id
    
    def assign_task_to_worker(self, task_id, worker_id):
        """Assign a task to a specific worker."""
        if task_id not in self.tasks or worker_id not in self.workers:
            return None
        
        task = self.tasks[task_id]
        worker = self.workers[worker_id]
        
        if worker['status'] != 'available':
            return None
        
        task['assigned_worker'] = worker_id
        worker['status'] = 'busy'
        worker['current_task'] = task_id
        self.worker_assignments[worker_id].append(task_id)
        
        return worker_id
    
    def get_worker_assignments(self):
        """Get current worker assignments."""
        return dict(self.worker_assignments)
    
    def get_task_status(self, task_id):
        """Get current task status."""
        task = self.tasks.get(task_id)
        return task['status'] if task else None
    
    def get_performance_metrics(self):
        """Get performance metrics."""
        metrics = self.performance_metrics.copy()
        if metrics['completed_tasks'] > 0:
            metrics['average_execution_time'] = metrics['total_execution_time'] / metrics['completed_tasks']
        else:
            metrics['average_execution_time'] = 0
        
        metrics['throughput'] = metrics['completed_tasks'] / max(1, time.time() - time.time() + 3600)  # per hour
        return metrics
    
    def get_task_schedule(self, task_id):
        """Get task schedule information."""
        task = self.tasks.get(task_id)
        if not task or not task.get('cron_schedule'):
            return None
        
        return {
            'type': 'cron',
            'expression': task['cron_schedule']
        }
    
    def get_next_execution_time(self, task_id):
        """Get next execution time for scheduled task."""
        task = self.tasks.get(task_id)
        if not task or not task.get('cron_schedule'):
            return 0
        
        # Simple implementation - in reality would parse cron expression
        return time.time() + 3600  # Next hour
    
    # Basic methods from previous levels
    def get_next_task(self):
        """Get the next available task."""
        for task_id in self.priority_queue:
            if self.can_execute(task_id):
                return task_id
        return None
    
    def can_execute(self, task_id):
        """Check if a task can be executed."""
        return True  # Simplified for this level
    
    def complete_task(self, task_id):
        """Mark a task as completed."""
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = 'completed'
            self.tasks[task_id]['completed_at'] = time.time()
            
            # Update worker status
            worker_id = self.tasks[task_id].get('assigned_worker')
            if worker_id and worker_id in self.workers:
                self.workers[worker_id]['status'] = 'available'
                self.workers[worker_id]['current_task'] = None
            
            # Update metrics
            self.performance_metrics['completed_tasks'] += 1
