"""
SPEED DRILL 5: Backup/Restore Operations
Implement the Database class to pass all tests.
"""

import copy


class Database:
    """
    A database with backup and restore functionality.
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize storage
    - set(self, key, value): Set a key-value pair
    - backup(self, backup_id): Create a backup
    - restore(self, backup_id): Restore from backup
    """
    
    def __init__(self):
        """Initialize the database."""
        # TODO: Implement storage for data and backups
        pass
    
    def set(self, key, value):
        """Set a key-value pair."""
        # TODO: Implement set operation
        pass
    
    def backup(self, backup_id):
        """Create a backup with given ID."""
        # TODO: Implement backup using deepcopy
        pass
    
    def restore(self, backup_id):
        """Restore from backup. Return True if successful."""
        # TODO: Implement restore using deepcopy
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    db = Database()
    print("Implement the Database class methods first!")
