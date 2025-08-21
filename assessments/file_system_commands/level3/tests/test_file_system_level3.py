import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from file_system_commands.level3.model_solution.file_system import FileSystemSimulator

class TestFileSystemLevel3:
    def test_file_upload_at(self):
        fs = FileSystemSimulator()
        
        # Test file upload with specific time
        result = fs.upload_file("future_file.txt", "100kb", timestamp=1000)
        assert "uploaded at" in result
        
        # Test file upload with past time
        result = fs.upload_file("past_file.txt", "100kb", timestamp=0)
        assert "uploaded at" in result
        
    def test_file_get_at(self):
        fs = FileSystemSimulator()
        
        # Upload file at specific time
        fs.upload_file("test.txt", "100kb", timestamp=1000)
        
        # Test getting file at different times
        result = fs.get_file("test.txt", timestamp=1000)
        assert "got at" in result
        
        result = fs.get_file("test.txt", timestamp=999)
        assert "file not found" in result
        
    def test_file_copy_at(self):
        fs = FileSystemSimulator()
        
        # Upload source file
        fs.upload_file("source.txt", "100kb", timestamp=1000)
        
        # Test copying at specific time
        result = fs.copy_file("source.txt", "copy.txt", timestamp=1000)
        assert "copied at" in result
        
        # Verify copy exists
        result = fs.get_file("copy.txt", timestamp=1000)
        assert "got at" in result
        
    def test_file_search_at(self):
        fs = FileSystemSimulator()
        
        # Upload files at different times
        fs.upload_file("file1.txt", "100kb", timestamp=1000)
        fs.upload_file("file2.txt", "100kb", timestamp=2000)
        
        # Test search at specific time
        result = fs.search_files("file", timestamp=1000)
        assert len(result) == 1
        assert "file1.txt" in result
        
        result = fs.search_files("file", timestamp=2000)
        assert len(result) == 2  # Both files should be available
        
    def test_time_based_file_operations(self):
        fs = FileSystemSimulator()
        
        # Upload file at time 1000
        fs.upload_file("temporal.txt", "100kb", timestamp=1000)
        
        # Test operations at different times
        # At time 999 - file shouldn't exist
        result = fs.get_file("temporal.txt", timestamp=999)
        assert "file not found" in result
        
        # At time 1000 - file should exist
        result = fs.get_file("temporal.txt", timestamp=1000)
        assert "got at" in result
        
        # At time 2000 - file should still exist
        result = fs.get_file("temporal.txt", timestamp=2000)
        assert "got at" in result
