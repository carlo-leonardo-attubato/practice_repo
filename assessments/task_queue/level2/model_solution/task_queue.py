"""
LEVEL 2: Enhanced Task Queue Features - MODEL SOLUTION
Task priorities, categories, dependencies, and timeouts.
"""

import time
import uuid
from collections import defaultdict, deque


class TaskQueue:
    """Enhanced task queue with priorities and categories."""
    
    def __init__(self):
        """Initialize the enhanced task queue."""
        self.tasks = {}  # task_id -> task_data
        self.priority_queue = deque()  # Priority-based queue
        self.categories = defaultdict(list)  # category -> task_ids
        self.dependencies = defaultdict(list)  # task_id -> dependency_list
        self.dependent_on = defaultdict(list)  # task_id -> tasks_that_depend_on_this
        self.next_task_id = 1
    
    def add_task(self, name, priority=5, category="default", dependencies=None, timeout=None):
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
            'retry_count': 0
        }
        
        self.tasks[task_id] = task
        
        # Add to priority queue
        self._add_to_priority_queue(task_id)
        
        # Add to category
        self.categories[category].append(task_id)
        
        # Handle dependencies
        if dependencies:
            self.dependencies[task_id] = dependencies
            for dep_id in dependencies:
                if dep_id in self.tasks:
                    self.dependent_on[dep_id].append(task_id)
        
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
    
    def get_next_task(self):
        """Get the next available task."""
        for task_id in self.priority_queue:
            if self.can_execute(task_id):
                return task_id
        return None
    
    def can_execute(self, task_id):
        """Check if a task can be executed (dependencies met)."""
        if task_id not in self.dependencies:
            return True
        
        for dep_id in self.dependencies[task_id]:
            if dep_id not in self.tasks or self.tasks[dep_id]['status'] != 'completed':
                return False
        
        return True
    
    def complete_task(self, task_id):
        """Mark a task as completed."""
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = 'completed'
            self.tasks[task_id]['completed_at'] = time.time()
            
            # Remove from priority queue
            if task_id in self.priority_queue:
                self.priority_queue.remove(task_id)
            
            # Check dependent tasks
            for dependent_id in self.dependent_on[task_id]:
                if self.can_execute(dependent_id):
                    # Task can now be executed
                    pass
    
    def get_tasks_by_category(self, category):
        """Get all tasks in a specific category."""
        task_ids = self.categories.get(category, [])
        return [self.tasks[task_id] for task_id in task_ids if task_id in self.tasks]
    
    def get_all_tasks(self):
        """Get all tasks sorted by priority."""
        return [self.tasks[task_id] for task_id in self.priority_queue]
    
    def is_task_expired(self, task_id):
        """Check if a task has expired."""
        task = self.tasks.get(task_id)
        if not task or not task.get('timeout'):
            return False
        
        return time.time() - task['created_at'] > task['timeout']
