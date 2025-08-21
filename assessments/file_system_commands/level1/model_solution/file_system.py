"""
LEVEL 1: Basic File Operations - MODEL SOLUTION
Command-driven file system with basic operations.
"""

import time


class FileSystemSimulator:
    """Command-driven file system simulator."""
    
    def __init__(self):
        """Initialize the file system."""
        self.files = {}  # filename -> file_data
    
    def upload_file(self, filename, size):
        """Upload a file to the system. Returns success status."""
        self.files[filename] = {
            'filename': filename,
            'size': size,
            'uploaded_at': time.time()
        }
        return True  # Success
    
    def get_file(self, filename):
        """Retrieve a file from the system. Returns file data or None."""
        if filename not in self.files:
            return None
        
        return self.files[filename]  # Return actual file data
    
    def copy_file(self, source, dest):
        """Copy a file to a new name. Returns success status."""
        if source not in self.files:
            return False  # Failure
        
        # Create copy with same data
        source_file = self.files[source]
        self.files[dest] = {
            'filename': dest,
            'size': source_file['size'],
            'uploaded_at': time.time()
        }
        
        return True  # Success
    
    def file_exists(self, filename):
        """Check if a file exists. Returns boolean."""
        return filename in self.files
    
    def search_files(self, query):
        """Search for files by name prefix. Returns list of filenames."""
        matching_files = []
        for filename in self.files:
            if query in filename:
                matching_files.append(filename)
        
        # Sort for consistent test results
        matching_files.sort()
        return matching_files  # Return actual list


def simulate_coding_framework(commands):
    """
    MAIN FUNCTION: Parse commands and execute file operations.
    This is the EXACT pattern Anthropic uses.
    
    Now properly separates return values from logging:
    - Methods return actual data
    - Framework handles logging and formatting
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


if __name__ == "__main__":
    # Test with the exact Reddit example
    test_commands = [
        ["FILE_UPLOAD", "Cars.txt", "200kb"],
        ["FILE_GET", "Cars.txt"],
        ["FILE_COPY", "Cars.txt", "Cars2.txt"],
        ["FILE_GET", "Cars2.txt"]
    ]
    
    print("🎯 Testing Level 1 File System Commands")
    print("="*50)
    print("Commands:", test_commands)
    print()
    
    results = simulate_coding_framework(test_commands)
    expected = ["uploaded Cars.txt", "got Cars.txt", "copied Cars.txt to Cars2.txt", "got Cars2.txt"]
    
    print("Results:", results)
    print("Expected:", expected)
    print("Match:", results == expected)
    
    if results == expected:
        print("✅ Level 1 implementation PERFECT!")
    else:
        print("❌ Need to fix implementation")
    
    print("\nThis is the EXACT Anthropic CodeSignal pattern!")
    print("Now with proper OOP: methods return data, framework handles logging!")
