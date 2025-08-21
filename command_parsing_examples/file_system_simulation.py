"""
ANTHROPIC CODESIGNAL PATTERN: Command Parsing to OOP Conversion
This shows how to convert the weird command parsing format to familiar OOP.
"""

import time
from datetime import datetime
from typing import List, Dict, Any, Optional


class FileSystemSimulator:
    """
    The OOP version of what the command parser does.
    This is the familiar pattern you understand.
    """
    
    def __init__(self):
        self.files = {}  # filename -> file_data
        self.upload_history = []  # For rollback functionality
    
    def upload_file(self, filename: str, size: str, timestamp: float = None, ttl_seconds: int = None):
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
    
    def get_file(self, filename: str, timestamp: float = None) -> Optional[str]:
        """Get a file if it exists and hasn't expired."""
        current_time = timestamp or time.time()
        
        if filename not in self.files:
            return "file not found"
        
        file_data = self.files[filename]
        
        # Check if file has expired
        if file_data['expires_at'] and current_time > file_data['expires_at']:
            return "file not found"
        
        return f"got{' at' if timestamp else ''} {filename}"
    
    def copy_file(self, source: str, dest: str, timestamp: float = None) -> Optional[str]:
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
    
    def search_files(self, query: str, timestamp: float = None) -> str:
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
        
        # Sort alphabetically (as shown in test)
        matching_files.sort()
        
        return f"found{' at' if timestamp else ''} {matching_files}"
    
    def rollback_to_time(self, target_time: float) -> str:
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


def simulate_coding_framework(commands: List[List[str]]) -> List[str]:
    """
    THE COMMAND PARSER - This is what CodeSignal expects you to write.
    This converts commands to OOP method calls.
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
            
        elif cmd_type == "ROLLBACK":
            # ["ROLLBACK", "2021-07-01T12:10:00"]
            timestamp_str = command[1]
            timestamp = datetime.fromisoformat(timestamp_str).timestamp()
            
            result = fs.rollback_to_time(timestamp)
            results.append(result)
    
    return results


# =================== THE KEY INSIGHT ===================

def convert_commands_to_oop_calls(commands: List[List[str]]) -> str:
    """
    Shows you how command parsing translates to familiar OOP method calls.
    Study this to understand the conversion!
    """
    
    oop_code = []
    oop_code.append("fs = FileSystemSimulator()")
    oop_code.append("results = []")
    oop_code.append("")
    
    for i, command in enumerate(commands):
        cmd_type = command[0]
        oop_code.append(f"# Command {i+1}: {command}")
        
        if cmd_type == "FILE_UPLOAD":
            filename, size = command[1], command[2]
            oop_code.append(f"result = fs.upload_file('{filename}', '{size}')")
            
        elif cmd_type == "FILE_GET":
            filename = command[1]
            oop_code.append(f"result = fs.get_file('{filename}')")
            
        elif cmd_type == "FILE_COPY":
            source, dest = command[1], command[2]
            oop_code.append(f"result = fs.copy_file('{source}', '{dest}')")
            
        elif cmd_type == "FILE_SEARCH":
            query = command[1]
            oop_code.append(f"result = fs.search_files('{query}')")
            
        elif cmd_type == "ROLLBACK":
            timestamp_str = command[1]
            oop_code.append(f"result = fs.rollback_to_time(datetime.fromisoformat('{timestamp_str}').timestamp())")
        
        oop_code.append("results.append(result)")
        oop_code.append("")
    
    return "\n".join(oop_code)


if __name__ == "__main__":
    # Test the conversion
    test_commands = [
        ["FILE_UPLOAD", "Cars.txt", "200kb"],
        ["FILE_GET", "Cars.txt"],
        ["FILE_COPY", "Cars.txt", "Cars2.txt"],
        ["FILE_SEARCH", "Car"]
    ]
    
    print("🎯 COMMAND PARSING PATTERN")
    print("="*50)
    print("Commands:", test_commands)
    print()
    
    print("🔄 CONVERTED TO FAMILIAR OOP:")
    print("="*50)
    print(convert_commands_to_oop_calls(test_commands))
    print()
    
    print("📋 ACTUAL EXECUTION:")
    print("="*50)
    results = simulate_coding_framework(test_commands)
    for i, result in enumerate(results):
        print(f"Result {i+1}: {result}")
    
    print("\n✅ This is the EXACT pattern Anthropic uses!")
    print("Practice converting commands → OOP method calls → results!")
