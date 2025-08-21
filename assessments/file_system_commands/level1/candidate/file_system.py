"""
LEVEL 1: Basic File Operations
Implement command-driven file system with basic operations.

Time Limit: 15-20 minutes
Points: ~100 points

Requirements:
- Parse FILE_UPLOAD, FILE_GET, FILE_COPY commands
- Track files with names and sizes
- Return formatted response strings
- Basic file storage and retrieval
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
            str: "uploaded {filename}"
        """
        # TODO: Implement file upload
        pass
    
    def get_file(self, filename):
        """
        Retrieve a file from the system.
        
        Args:
            filename (str): Name of the file to retrieve
            
        Returns:
            str: "got {filename}" or "file not found"
        """
        # TODO: Implement file retrieval
        pass
    
    def copy_file(self, source, dest):
        """
        Copy a file to a new name.
        
        Args:
            source (str): Source filename
            dest (str): Destination filename
            
        Returns:
            str: "copied {source} to {dest}" or error message
        """
        # TODO: Implement file copying
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


def simulate_coding_framework(commands):
    """
    MAIN FUNCTION: Parse commands and execute file operations.
    This is what CodeSignal expects you to implement.
    
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
            result = fs.upload_file(filename, size)
            results.append(result)
            
        elif cmd_type == "FILE_GET":
            # ["FILE_GET", "Cars.txt"]
            filename = command[1]
            result = fs.get_file(filename)
            results.append(result)
            
        elif cmd_type == "FILE_COPY":
            # ["FILE_COPY", "Cars.txt", "Cars2.txt"]
            source, dest = command[1], command[2]
            result = fs.copy_file(source, dest)
            results.append(result)
    
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
    print("Expected output: ['uploaded Cars.txt', 'got Cars.txt', 'copied Cars.txt to Cars2.txt', 'got Cars2.txt']")
