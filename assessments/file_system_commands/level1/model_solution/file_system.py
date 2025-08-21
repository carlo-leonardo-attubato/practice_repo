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
        """Upload a file to the system."""
        self.files[filename] = {
            'filename': filename,
            'size': size,
            'uploaded_at': time.time()
        }
        return f"uploaded {filename}"
    
    def get_file(self, filename):
        """Retrieve a file from the system."""
        if filename not in self.files:
            return "file not found"
        
        return f"got {filename}"
    
    def copy_file(self, source, dest):
        """Copy a file to a new name."""
        if source not in self.files:
            return "source file not found"
        
        # Create copy with same data
        source_file = self.files[source]
        self.files[dest] = {
            'filename': dest,
            'size': source_file['size'],
            'uploaded_at': time.time()
        }
        
        return f"copied {source} to {dest}"
    
    def file_exists(self, filename):
        """Check if a file exists."""
        return filename in self.files
    
    def search_files(self, query):
        """Search for files by name prefix."""
        matching_files = []
        for filename in self.files:
            if query in filename:
                matching_files.append(filename)
        
        # Sort for consistent test results
        matching_files.sort()
        
        if matching_files:
            return f"found {matching_files}"
        else:
            return "found []"


def simulate_coding_framework(commands):
    """
    MAIN FUNCTION: Parse commands and execute file operations.
    This is the EXACT pattern Anthropic uses.
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
            
        elif cmd_type == "FILE_SEARCH":
            # ["FILE_SEARCH", "Ba"]
            query = command[1]
            result = fs.search_files(query)
            results.append(result)
    
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
