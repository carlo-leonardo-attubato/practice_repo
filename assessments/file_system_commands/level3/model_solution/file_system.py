"""
LEVEL 3: Time-based Operations - MODEL SOLUTION
Command-driven file system with TTL and timestamp operations.
"""

import time
from datetime import datetime


class FileSystemSimulator:
    """Advanced file system simulator with TTL and timestamps."""
    
    def __init__(self):
        """Initialize the file system."""
        self.files = {}  # filename -> file_data
        self.upload_history = []  # For rollback functionality
    
    # =================== LEVEL 1-2 METHODS ===================
    
    def upload_file(self, filename, size, timestamp=None, ttl_seconds=None):
        """Upload a file with optional TTL."""
        current_time = timestamp or time.time()
        
        file_data = {
            'filename': filename,
            'size': size,
            'uploaded_at': current_time,
            'expires_at': current_time + ttl_seconds if ttl_seconds else None
        }
        
        self.files[filename] = file_data
        self.upload_history.append({
            'action': 'upload',
            'filename': filename,
            'timestamp': current_time,
            'data': file_data.copy()
        })
        
        return f"uploaded{' at' if timestamp else ''} {filename}"
    
    def get_file(self, filename, timestamp=None):
        """Get a file if it exists and hasn't expired."""
        current_time = timestamp or time.time()
        
        if filename not in self.files:
            return "file not found"
        
        file_data = self.files[filename]
        
        # Check if file has expired
        if file_data['expires_at'] and current_time > file_data['expires_at']:
            return "file not found"
        
        return f"got{' at' if timestamp else ''} {filename}"
    
    def copy_file(self, source, dest, timestamp=None):
        """Copy a file if source exists and hasn't expired."""
        current_time = timestamp or time.time()
        
        if source not in self.files:
            return "source file not found"
        
        source_file = self.files[source]
        
        # Check if source has expired
        if source_file['expires_at'] and current_time > source_file['expires_at']:
            return "source file not found"
        
        # Create copy
        self.files[dest] = {
            'filename': dest,
            'size': source_file['size'],
            'uploaded_at': current_time,
            'expires_at': source_file['expires_at']  # Copy expiration
        }
        
        self.upload_history.append({
            'action': 'copy',
            'filename': dest,
            'timestamp': current_time,
            'data': self.files[dest].copy()
        })
        
        return f"copied{' at' if timestamp else ''} {source} to {dest}"
    
    def search_files(self, query, timestamp=None):
        """Search for files by name prefix."""
        current_time = timestamp or time.time()
        
        matching_files = []
        for filename, file_data in self.files.items():
            # Check if file hasn't expired
            if file_data['expires_at'] and current_time > file_data['expires_at']:
                continue
            
            # Check if filename starts with query
            if filename.startswith(query):
                matching_files.append(filename)
        
        # Sort alphabetically (as shown in Reddit test)
        matching_files.sort()
        
        return f"found{' at' if timestamp else ''} {matching_files}"
    
    def file_exists(self, filename, timestamp=None):
        """Check if file exists and hasn't expired."""
        current_time = timestamp or time.time()
        
        if filename not in self.files:
            return False
        
        file_data = self.files[filename]
        if file_data['expires_at'] and current_time > file_data['expires_at']:
            return False
        
        return True


def simulate_coding_framework(commands):
    """
    MAIN FUNCTION: Parse commands and execute operations.
    This is the EXACT pattern from the Reddit post.
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
            
        elif cmd_type == "FILE_UPLOAD_AT":
            # ["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "Python.txt", "150kb"]
            # or ["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "CodeSignal.txt", "150kb", 3600]
            timestamp_str, filename, size = command[1], command[2], command[3]
            ttl_seconds = int(command[4]) if len(command) > 4 else None
            
            # Parse timestamp
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            
            result = fs.upload_file(filename, size, timestamp, ttl_seconds)
            results.append(result)
            
        elif cmd_type == "FILE_GET_AT":
            # ["FILE_GET_AT", "2021-07-01T13:00:01", "Python.txt"]
            timestamp_str, filename = command[1], command[2]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            
            result = fs.get_file(filename, timestamp)
            results.append(result)
            
        elif cmd_type == "FILE_COPY_AT":
            # ["FILE_COPY_AT", "2021-07-01T12:00:00", "Python.txt", "PythonCopy.txt"]
            timestamp_str, source, dest = command[1], command[2], command[3]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            
            result = fs.copy_file(source, dest, timestamp)
            results.append(result)
            
        elif cmd_type == "FILE_SEARCH_AT":
            # ["FILE_SEARCH_AT", "2021-07-01T12:00:00", "Py"]
            timestamp_str, query = command[1], command[2]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            
            result = fs.search_files(query, timestamp)
            results.append(result)
    
    return results


if __name__ == "__main__":
    # Test with the EXACT Reddit examples
    print("🎯 Testing EXACT Anthropic Pattern from Reddit")
    print("="*60)
    
    # Test Group 1 (Level 1)
    test_data_1 = [
        ["FILE_UPLOAD", "Cars.txt", "200kb"], 
        ["FILE_GET", "Cars.txt"], 
        ["FILE_COPY", "Cars.txt", "Cars2.txt"], 
        ["FILE_GET", "Cars2.txt"]
    ]
    
    results_1 = simulate_coding_framework(test_data_1)
    expected_1 = ["uploaded Cars.txt", "got Cars.txt", "copied Cars.txt to Cars2.txt", "got Cars2.txt"]
    
    print("Test 1 Results:", results_1)
    print("Test 1 Expected:", expected_1)
    print("Test 1 Match:", results_1 == expected_1)
    print()
    
    # Test Group 2 (Level 2 - Search)
    test_data_2 = [
        ["FILE_UPLOAD", "Foo.txt", "100kb"], 
        ["FILE_UPLOAD", "Bar.csv", "200kb"], 
        ["FILE_UPLOAD", "Baz.pdf", "300kb"],
        ["FILE_SEARCH", "Ba"]
    ]
    
    results_2 = simulate_coding_framework(test_data_2)
    expected_2 = ["uploaded Foo.txt", "uploaded Bar.csv", "uploaded Baz.pdf", "found ['Bar.csv', 'Baz.pdf']"]
    
    print("Test 2 Results:", results_2)
    print("Test 2 Expected:", expected_2)
    print("Test 2 Match:", str(results_2) == str(expected_2))
    print()
    
    print("✅ This is the EXACT Anthropic CodeSignal pattern!")
    print("Practice this command → OOP conversion!")
