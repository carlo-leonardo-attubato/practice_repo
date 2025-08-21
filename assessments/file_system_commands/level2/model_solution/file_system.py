"""
LEVEL 2: File Search Operations - MODEL SOLUTION
Enhanced file operations with search capabilities.
"""

import time
from collections import defaultdict


class FileSystem:
    """File system with search capabilities."""
    
    def __init__(self):
        """Initialize the file system."""
        self.files = {}  # filename -> file_data
        self.file_index = defaultdict(list)  # search_term -> [filenames]
    
    def execute_command(self, command):
        """Execute a file system command."""
        if not command or len(command) < 1:
            return "Invalid command"
        
        cmd = command[0]
        
        if cmd == "FILE_UPLOAD":
            if len(command) >= 3:
                filename, size = command[1], command[2]
                return self._upload_file(filename, size)
            return "Invalid FILE_UPLOAD command"
        
        elif cmd == "FILE_GET":
            if len(command) >= 2:
                filename = command[1]
                return self._get_file(filename)
            return "Invalid FILE_GET command"
        
        elif cmd == "FILE_COPY":
            if len(command) >= 3:
                source, destination = command[1], command[2]
                return self._copy_file(source, destination)
            return "Invalid FILE_COPY command"
        
        elif cmd == "FILE_SEARCH":
            if len(command) >= 2:
                query = command[1]
                extension = command[2] if len(command) >= 3 else None
                return self._search_files(query, extension)
            return "Invalid FILE_SEARCH command"
        
        else:
            return f"Unknown command: {cmd}"
    
    def _upload_file(self, filename, size):
        """Upload a file."""
        if filename in self.files:
            return f"File '{filename}' already exists"
        
        self.files[filename] = {
            'name': filename,
            'size': size,
            'uploaded_at': time.time()
        }
        
        # Index the file for search
        self._index_file(filename)
        
        return f"File '{filename}' uploaded successfully"
    
    def _get_file(self, filename):
        """Get file information."""
        if filename not in self.files:
            return f"File '{filename}' not found"
        
        file_info = self.files[filename]
        return f"File: {file_info['name']}, Size: {file_info['size']}, Uploaded: {file_info['uploaded_at']}"
    
    def _copy_file(self, source, destination):
        """Copy a file."""
        if source not in self.files:
            return f"Source file '{source}' not found"
        
        if destination in self.files:
            return f"Destination file '{destination}' already exists"
        
        # Copy file data
        source_data = self.files[source]
        self.files[destination] = {
            'name': destination,
            'size': source_data['size'],
            'uploaded_at': time.time(),
            'copied_from': source
        }
        
        # Index the new file
        self._index_file(destination)
        
        return f"File '{source}' copied to '{destination}'"
    
    def _search_files(self, query, extension=None):
        """Search for files."""
        if not query:
            # Return all files if no query
            return list(self.files.values())
        
        # Get candidates from index
        candidates = set()
        query_lower = query.lower()
        
        for filename in self.files:
            if query_lower in filename.lower():
                candidates.add(filename)
        
        # Filter by extension if specified
        if extension:
            extension_lower = extension.lower()
            candidates = {f for f in candidates if f.lower().endswith(extension_lower)}
        
        # Return file data for matching files
        return [self.files[filename] for filename in candidates]
    
    def _index_file(self, filename):
        """Index a file for search."""
        # Index by filename parts
        parts = filename.lower().split('.')
        for part in parts:
            if part:
                self.file_index[part].append(filename)
        
        # Index by full filename
        self.file_index[filename.lower()].append(filename)
