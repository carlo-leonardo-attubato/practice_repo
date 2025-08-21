"""
SPEED DRILL 2: Nested Dictionary Pattern
Implement the UserStore class to pass all tests.
"""

from collections import defaultdict


class UserStore:
    """
    A user data store using nested dictionaries.
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize storage
    - add_user_field(self, user_id, field, value): Add/update user field
    - get_user_field(self, user_id, field): Get user field value
    - get_all_users_with_field(self, field, value): Find users with specific field value
    """
    
    def __init__(self):
        """Initialize the user store."""
        # TODO: Use defaultdict(dict) for nested structure
        
        self.users = defaultdict(dict)
    
    def add_user_field(self, user_id, field, value):
        """Add or update a field for a user."""
        # TODO: Implement nested dictionary update

        self.users[user_id][field] = value

    def get_user_field(self, user_id, field):
        """Get a field value for a user. Return None if not found."""
        # TODO: Implement nested dictionary access
        self.users[user_id].get(field)

    
    def get_all_users_with_field(self, field, value):
        """Find all users with a specific field value."""
        # TODO: Implement filtering with list comprehension

        return [user_id for user_id in self.users.keys() if self.users[user_id][field] == value]

# Quick test - uncomment when ready
if __name__ == "__main__":
    store = UserStore()
    print("Implement the UserStore class methods first!")
