"""
LEVEL 1: Basic File Operations
Implement command-driven file system with basic operations.

Time Limit: 15-20 minutes
Points: ~100 points

Requirements:
- Parse FILE_UPLOAD, FILE_GET, FILE_COPY commands
- Track files with names and sizes
- Return actual data (not log messages)
- Basic file storage and retrieval

IMPORTANT: Methods should return actual data, not formatted strings!
The framework will handle logging and formatting.
"""

import time


class FileSystemSimulator:
    """
    Command-driven file system simulator.
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize the file system
    - upload_file(self, filename, size): Upload a file
    - get_file(self, filename): Retrieve a file
    - copy_file(self, source, dest): Copy a file
    - file_exists(self, filename): Check if file exists
    - search_files(self, query): Search for files
    """
    
    def __init__(self):
        """Initialize the file system."""
        # TODO: Initialize storage for files
        pass
    
    def upload_file(self, filename, size):
        """
        Upload a file to the system.
        
        Args:
            filename (str): Name of the file
            size (str): Size of the file (e.g., "200kb")
            
        Returns:
            bool: True if successful, False if failed
        """
        # TODO: Implement file upload
        # Store file data and return success status
        pass
    
    def get_file(self, filename):
        """
        Retrieve a file from the system.
        
        Args:
            filename (str): Name of the file to retrieve
            
        Returns:
            dict: File data if found, None if not found
        """
        # TODO: Implement file retrieval
        # Return actual file data, not a string message
        pass
    
    def copy_file(self, source, dest):
        """
        Copy a file to a new name.
        
        Args:
            source (str): Source filename
            dest (str): Destination filename
            
        Returns:
            bool: True if successful, False if source not found
        """
        # TODO: Implement file copying
        # Return success status, not a string message
        pass
    
    def file_exists(self, filename):
        """
        Check if a file exists.
        
        Args:
            filename (str): Filename to check
            
        Returns:
            bool: True if file exists
        """
        # TODO: Implement file existence check
        pass
    
    def search_files(self, query):
        """
        Search for files by name prefix.
        
        Args:
            query (str): Search query
            
        Returns:
            list: List of matching filenames
        """
        # TODO: Implement file search
        # Return actual list of filenames, not a formatted string
        pass


def simulate_coding_framework(commands):
    """
    MAIN FUNCTION: Parse commands and execute file operations.
    This is what CodeSignal expects you to implement.
    
    IMPORTANT: This function handles the logging and formatting.
    Your methods should return actual data!
    
    Args:
        commands (list): List of command arrays
        
    Returns:
        list: List of result strings
    """
    
    fs = FileSystemSimulator()
    results = []
    
    for command in commands:
        cmd_type = command[0]
        
        if cmd_type == "FILE_UPLOAD":
            # ["FILE_UPLOAD", "Cars.txt", "200kb"]
            filename, size = command[1], command[2]
            success = fs.upload_file(filename, size)
            if success:
                results.append(f"uploaded {filename}")
            else:
                results.append(f"failed to upload {filename}")
            
        elif cmd_type == "FILE_GET":
            # ["FILE_GET", "Cars.txt"]
            filename = command[1]
            file_data = fs.get_file(filename)
            if file_data:
                results.append(f"got {filename}")
            else:
                results.append("file not found")
            
        elif cmd_type == "FILE_COPY":
            # ["FILE_COPY", "Cars.txt", "Cars2.txt"]
            source, dest = command[1], command[2]
            success = fs.copy_file(source, dest)
            if success:
                results.append(f"copied {source} to {dest}")
            else:
                results.append("source file not found")
            
        elif cmd_type == "FILE_SEARCH":
            # ["FILE_SEARCH", "Ba"]
            query = command[1]
            matching_files = fs.search_files(query)
            if matching_files:
                results.append(f"found {matching_files}")
            else:
                results.append("found []")
    
    return results


# Quick test - uncomment when ready
if __name__ == "__main__":
    # Test with the exact Reddit example
    test_commands = [
        ["FILE_UPLOAD", "Cars.txt", "200kb"],
        ["FILE_GET", "Cars.txt"],
        ["FILE_COPY", "Cars.txt", "Cars2.txt"],
        ["FILE_GET", "Cars2.txt"]
    ]
    
    print("Level 1: Implement the FileSystemSimulator class methods!")
    print("IMPORTANT: Methods should return actual data, not log messages!")
    print("Expected output: ['uploaded Cars.txt', 'got Cars.txt', 'copied Cars.txt to Cars2.txt', 'got Cars2.txt']")
    print("\nKey changes:")
    print("- upload_file() returns bool (success status)")
    print("- get_file() returns file data or None")
    print("- copy_file() returns bool (success status)")
    print("- search_files() returns list of filenames")
    print("- Framework handles all logging and formatting!")
