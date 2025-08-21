"""
LEVEL 1: Basic Task Management
Implement core task queue operations.

Time Limit: 15-20 minutes
Points: ~100 points

Requirements:
- Add tasks to queue with priorities
- Mark tasks as complete
- Get pending tasks
- Basic task information and queue management
"""

from collections import deque


class TaskQueue:
    """
    Basic task queue system.
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize the task queue
    - add_task(self, title, description, priority): Add a new task
    - get_task(self, task_id): Get task information
    - complete_task(self, task_id): Mark task as completed
    - get_pending_tasks(self): Get all pending tasks
    - get_next_task(self): Get next task to process
    - get_task_count(self): Get total number of tasks
    - get_pending_count(self): Get number of pending tasks
    """
    
    def __init__(self):
        """Initialize the task queue."""
        # TODO: Initialize storage for tasks and queue
        pass
    
    def add_task(self, title, description, priority=1):
        """
        Add a new task to the queue.
        
        Args:
            title (str): Task title
            description (str): Task description
            priority (int): Task priority (higher = more important)
            
        Returns:
            str: Task ID if successful, None if failed
        """
        # TODO: Implement task addition
        pass
    
    def get_task(self, task_id):
        """
        Get task information.
        
        Args:
            task_id (str): Task identifier
            
        Returns:
            dict: Task data if found, None if not found
        """
        # TODO: Implement task retrieval
        pass
    
    def complete_task(self, task_id):
        """
        Mark a task as completed.
        
        Args:
            task_id (str): Task identifier
            
        Returns:
            bool: True if marked complete, False if task not found
        """
        # TODO: Implement task completion
        pass
    
    def get_pending_tasks(self):
        """
        Get all pending tasks.
        
        Returns:
            list: List of pending tasks
        """
        # TODO: Implement pending task retrieval
        pass
    
    def get_next_task(self):
        """
        Get the next task to process (highest priority).
        
        Returns:
            dict: Next task data, None if no pending tasks
        """
        # TODO: Implement next task retrieval
        pass
    
    def get_task_count(self):
        """
        Get total number of tasks.
        
        Returns:
            int: Total task count
        """
        # TODO: Implement task counting
        pass
    
    def get_pending_count(self):
        """
        Get number of pending tasks.
        
        Returns:
            int: Number of pending tasks
        """
        # TODO: Implement pending task counting
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    queue = TaskQueue()
    print("Level 1: Implement the TaskQueue class methods!")
