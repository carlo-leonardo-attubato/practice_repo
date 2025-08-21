"""
LEVEL 1: Basic Task Management - MODEL SOLUTION
Core task operations and queue management.
"""

import time
from collections import deque


class TaskQueue:
    """Basic task queue system."""
    
    def __init__(self):
        """Initialize the task queue."""
        self.tasks = {}  # task_id -> task_data
        self.queue = deque()  # task_ids in order
        self.task_id_counter = 1
    
    def add_task(self, title, description, priority=1):
        """Add a new task to the queue."""
        task_id = str(self.task_id_counter)
        self.task_id_counter += 1
        
        task = {
            'task_id': task_id,
            'title': title,
            'description': description,
            'priority': priority,
            'status': 'pending',
            'created_at': time.time(),
            'completed_at': None
        }
        
        self.tasks[task_id] = task
        self.queue.append(task_id)
        return task_id
    
    def get_task(self, task_id):
        """Get task information."""
        return self.tasks.get(task_id)
    
    def complete_task(self, task_id):
        """Mark a task as completed."""
        if task_id not in self.tasks:
            return False
        
        self.tasks[task_id]['status'] = 'completed'
        self.tasks[task_id]['completed_at'] = time.time()
        
        # Remove from queue if present
        try:
            self.queue.remove(task_id)
        except ValueError:
            pass  # Task not in queue
        
        return True
    
    def get_pending_tasks(self):
        """Get all pending tasks."""
        return [self.tasks[task_id] for task_id in self.queue if task_id in self.tasks]
    
    def get_next_task(self):
        """Get the next task to process."""
        while self.queue:
            task_id = self.queue.popleft()
            if task_id in self.tasks and self.tasks[task_id]['status'] == 'pending':
                return self.tasks[task_id]
        return None
    
    def get_task_count(self):
        """Get total number of tasks."""
        return len(self.tasks)
    
    def get_pending_count(self):
        """Get number of pending tasks."""
        return len(self.queue)
