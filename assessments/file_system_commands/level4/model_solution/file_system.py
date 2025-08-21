"""
LEVEL 4: System State Management - MODEL SOLUTION
Command-driven file system with rollback functionality.
"""

import time
import copy
from datetime import datetime


class FileSystemSimulator:
    """Complete file system simulator with rollback."""
    
    def __init__(self):
        """Initialize the file system."""
        self.files = {}  # filename -> file_data
        self.upload_history = []  # For rollback functionality
    
    # =================== LEVEL 1-3 METHODS ===================
    
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
        
        # Sort alphabetically
        matching_files.sort()
        
        return f"found{' at' if timestamp else ''} {matching_files}"
    
    # =================== LEVEL 4 NEW METHODS ===================
    
    def rollback_to_time(self, target_time):
        """Rollback system state to a specific time."""
        # Remove all files uploaded after target time
        files_to_remove = []
        for filename, file_data in self.files.items():
            if file_data['uploaded_at'] > target_time:
                files_to_remove.append(filename)
        
        for filename in files_to_remove:
            del self.files[filename]
        
        # Clean up history
        self.upload_history = [
            entry for entry in self.upload_history 
            if entry['timestamp'] <= target_time
        ]
        
        return f"rollback to {datetime.fromtimestamp(target_time).strftime('%Y-%m-%dT%H:%M:%S')}"


def simulate_coding_framework(commands):
    """
    MAIN FUNCTION: Parse ALL commands including rollback.
    This handles the complete Anthropic pattern.
    """
    
    fs = FileSystemSimulator()
    results = []
    
    for command in commands:
        cmd_type = command[0]
        
        if cmd_type == "FILE_UPLOAD":
            filename, size = command[1], command[2]
            result = fs.upload_file(filename, size)
            results.append(result)
            
        elif cmd_type == "FILE_GET":
            filename = command[1]
            result = fs.get_file(filename)
            results.append(result)
            
        elif cmd_type == "FILE_COPY":
            source, dest = command[1], command[2]
            result = fs.copy_file(source, dest)
            results.append(result)
            
        elif cmd_type == "FILE_SEARCH":
            query = command[1]
            result = fs.search_files(query)
            results.append(result)
            
        elif cmd_type == "FILE_UPLOAD_AT":
            timestamp_str, filename, size = command[1], command[2], command[3]
            ttl_seconds = int(command[4]) if len(command) > 4 else None
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            result = fs.upload_file(filename, size, timestamp, ttl_seconds)
            results.append(result)
            
        elif cmd_type == "FILE_GET_AT":
            timestamp_str, filename = command[1], command[2]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            result = fs.get_file(filename, timestamp)
            results.append(result)
            
        elif cmd_type == "FILE_COPY_AT":
            timestamp_str, source, dest = command[1], command[2], command[3]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            result = fs.copy_file(source, dest, timestamp)
            results.append(result)
            
        elif cmd_type == "FILE_SEARCH_AT":
            timestamp_str, query = command[1], command[2]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            result = fs.search_files(query, timestamp)
            results.append(result)
            
        elif cmd_type == "ROLLBACK":
            timestamp_str = command[1]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            result = fs.rollback_to_time(timestamp)
            results.append(result)
    
    return results


if __name__ == "__main__":
    # Test with ALL Reddit examples
    print("🎯 Testing COMPLETE Anthropic Pattern - All 4 Levels")
    print("="*70)
    
    # Test Group 4 (Complete with rollback)
    test_data_4 = [
        ["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "Initial.txt", "100kb"], 
        ["FILE_UPLOAD_AT", "2021-07-01T12:05:00", "Update1.txt", "150kb", 3600], 
        ["FILE_GET_AT", "2021-07-01T12:10:00", "Initial.txt"], 
        ["FILE_COPY_AT", "2021-07-01T12:15:00", "Update1.txt", "Update1Copy.txt"], 
        ["FILE_UPLOAD_AT", "2021-07-01T12:20:00", "Update2.txt", "200kb", 1800], 
        ["ROLLBACK", "2021-07-01T12:10:00"], 
        ["FILE_GET_AT", "2021-07-01T12:25:00", "Update1.txt"], 
        ["FILE_GET_AT", "2021-07-01T12:25:00", "Initial.txt"], 
        ["FILE_SEARCH_AT", "2021-07-01T12:25:00", "Up"],
        ["FILE_GET_AT", "2021-07-01T12:25:00", "Update2.txt"]
    ]
    
    results = simulate_coding_framework(test_data_4)
    expected = [
        "uploaded at Initial.txt", 
        "uploaded at Update1.txt", 
        "got at Initial.txt", 
        "copied at Update1.txt to Update1Copy.txt", 
        "uploaded at Update2.txt", 
        "rollback to 2021-07-01T12:10:00", 
        "got at Update1.txt", 
        "got at Initial.txt", 
        "found at ['Update1.txt', 'Update1Copy.txt', 'Update2.txt']", 
        "got at Update2.txt"
    ]
    
    print("Results:")
    for i, result in enumerate(results):
        print(f"  {i+1}. {result}")
    
    print("\nExpected:")
    for i, exp in enumerate(expected):
        print(f"  {i+1}. {exp}")
    
    print(f"\nMatch: {results == expected}")
    
    if results == expected:
        print("\n🎉 PERFECT! You've mastered the Anthropic pattern!")
    else:
        print("\n🔧 Debug needed - but you understand the pattern!")
    
    print("\n✅ This is EXACTLY what you'll see tomorrow!")
    print("Commands → OOP methods → Formatted results")
