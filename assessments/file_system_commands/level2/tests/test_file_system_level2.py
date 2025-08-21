import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from file_system_commands.level2.model_solution.file_system import FileSystem

class TestFileSystemLevel2:
    def test_file_search_basic(self):
        fs = FileSystem()
        
        # Upload some files
        fs.execute_command(["FILE_UPLOAD", "document.txt", "100kb"])
        fs.execute_command(["FILE_UPLOAD", "document.pdf", "200kb"])
        fs.execute_command(["FILE_UPLOAD", "image.jpg", "150kb"])
        
        # Test basic search
        result = fs.execute_command(["FILE_SEARCH", "document"])
        assert len(result) == 2
        assert any("document.txt" in str(f) for f in result)
        assert any("document.pdf" in str(f) for f in result)
        
    def test_file_search_by_extension(self):
        fs = FileSystem()
        
        # Upload files with different extensions
        fs.execute_command(["FILE_UPLOAD", "report.txt", "100kb"])
        fs.execute_command(["FILE_UPLOAD", "report.pdf", "200kb"])
        fs.execute_command(["FILE_UPLOAD", "report.doc", "150kb"])
        
        # Test search by extension
        result = fs.execute_command(["FILE_SEARCH", "report", "txt"])
        assert len(result) == 1
        assert "report.txt" in str(result[0])
        
    def test_file_search_case_insensitive(self):
        fs = FileSystem()
        
        # Upload files with different cases
        fs.execute_command(["FILE_UPLOAD", "Document.txt", "100kb"])
        fs.execute_command(["FILE_UPLOAD", "document.TXT", "100kb"])
        
        # Test case insensitive search
        result = fs.execute_command(["FILE_SEARCH", "document"])
        assert len(result) == 2
        
        result = fs.execute_command(["FILE_SEARCH", "DOCUMENT"])
        assert len(result) == 2
        
    def test_file_search_no_results(self):
        fs = FileSystem()
        
        # Upload a file
        fs.execute_command(["FILE_UPLOAD", "test.txt", "100kb"])
        
        # Test search with no results
        result = fs.execute_command(["FILE_SEARCH", "nonexistent"])
        assert len(result) == 0
        
    def test_file_search_empty_query(self):
        fs = FileSystem()
        
        # Upload some files
        fs.execute_command(["FILE_UPLOAD", "file1.txt", "100kb"])
        fs.execute_command(["FILE_UPLOAD", "file2.txt", "100kb"])
        
        # Test empty search query
        result = fs.execute_command(["FILE_SEARCH", ""])
        assert len(result) >= 2  # Should return all files
