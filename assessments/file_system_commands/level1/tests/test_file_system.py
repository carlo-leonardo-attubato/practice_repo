"""
Unit Tests for Level 1: Basic File Operations
Tests the EXACT Reddit examples from Anthropic CodeSignal.
"""

import pytest
import sys
import os

# Import configuration
from assessments.test_config import get_full_import_path

# Get the correct import path based on configuration
import_path = get_full_import_path('file_system_commands', 'level1')
exec(f"from {import_path} import simulate_coding_framework")


class TestFileSystemLevel1:
    """Test cases for Level 1 File System Commands."""
    
    def test_reddit_example_group_1(self):
        """Test the EXACT example from Reddit user who took Anthropic CodeSignal."""
        commands = [
            ["FILE_UPLOAD", "Cars.txt", "200kb"], 
            ["FILE_GET", "Cars.txt"], 
            ["FILE_COPY", "Cars.txt", "Cars2.txt"], 
            ["FILE_GET", "Cars2.txt"]
        ]
        
        results = simulate_coding_framework(commands)
        expected = ["uploaded Cars.txt", "got Cars.txt", "copied Cars.txt to Cars2.txt", "got Cars2.txt"]
        
        assert results == expected
    
    def test_reddit_example_group_2(self):
        """Test the search functionality from Reddit."""
        commands = [
            ["FILE_UPLOAD", "Foo.txt", "100kb"], 
            ["FILE_UPLOAD", "Bar.csv", "200kb"], 
            ["FILE_UPLOAD", "Baz.pdf", "300kb"],
            ["FILE_SEARCH", "Ba"]
        ]
        
        results = simulate_coding_framework(commands)
        expected = ["uploaded Foo.txt", "uploaded Bar.csv", "uploaded Baz.pdf", "found ['Bar.csv', 'Baz.pdf']"]
        
        assert results == expected
    
    def test_file_upload_basic(self):
        """Test basic file upload."""
        commands = [["FILE_UPLOAD", "test.txt", "100kb"]]
        results = simulate_coding_framework(commands)
        assert results == ["uploaded test.txt"]
    
    def test_file_get_existing(self):
        """Test getting existing file."""
        commands = [
            ["FILE_UPLOAD", "test.txt", "100kb"],
            ["FILE_GET", "test.txt"]
        ]
        results = simulate_coding_framework(commands)
        assert results == ["uploaded test.txt", "got test.txt"]
    
    def test_file_get_nonexistent(self):
        """Test getting non-existent file."""
        commands = [["FILE_GET", "nonexistent.txt"]]
        results = simulate_coding_framework(commands)
        assert results == ["file not found"]
    
    def test_file_copy_existing(self):
        """Test copying existing file."""
        commands = [
            ["FILE_UPLOAD", "original.txt", "100kb"],
            ["FILE_COPY", "original.txt", "copy.txt"],
            ["FILE_GET", "copy.txt"]
        ]
        results = simulate_coding_framework(commands)
        assert results == ["uploaded original.txt", "copied original.txt to copy.txt", "got copy.txt"]
    
    def test_file_copy_nonexistent(self):
        """Test copying non-existent file."""
        commands = [["FILE_COPY", "nonexistent.txt", "copy.txt"]]
        results = simulate_coding_framework(commands)
        assert results == ["source file not found"]
    
    def test_search_no_matches(self):
        """Test search with no matches."""
        commands = [
            ["FILE_UPLOAD", "test.txt", "100kb"],
            ["FILE_SEARCH", "xyz"]
        ]
        results = simulate_coding_framework(commands)
        assert results == ["uploaded test.txt", "found []"]
    
    def test_search_multiple_matches(self):
        """Test search with multiple matches."""
        commands = [
            ["FILE_UPLOAD", "test1.txt", "100kb"],
            ["FILE_UPLOAD", "test2.txt", "200kb"],
            ["FILE_UPLOAD", "other.txt", "300kb"],
            ["FILE_SEARCH", "test"]
        ]
        results = simulate_coding_framework(commands)
        expected = ["uploaded test1.txt", "uploaded test2.txt", "uploaded other.txt", "found ['test1.txt', 'test2.txt']"]
        assert results == expected
    
    def test_comprehensive_workflow(self):
        """Test complete Level 1 workflow."""
        commands = [
            ["FILE_UPLOAD", "doc1.txt", "50kb"],
            ["FILE_UPLOAD", "doc2.pdf", "100kb"],
            ["FILE_UPLOAD", "image1.jpg", "200kb"],
            ["FILE_GET", "doc1.txt"],
            ["FILE_COPY", "doc1.txt", "doc1_backup.txt"],
            ["FILE_SEARCH", "doc"],
            ["FILE_GET", "doc1_backup.txt"],
            ["FILE_GET", "nonexistent.txt"]
        ]
        
        results = simulate_coding_framework(commands)
        expected = [
            "uploaded doc1.txt",
            "uploaded doc2.pdf", 
            "uploaded image1.jpg",
            "got doc1.txt",
            "copied doc1.txt to doc1_backup.txt",
            "found ['doc1.txt', 'doc1_backup.txt', 'doc2.pdf']",
            "got doc1_backup.txt",
            "file not found"
        ]
        
        assert results == expected


def run_tests():
    """Run all tests and display results."""
    print("🧪 Level 1: Basic File Operations (EXACT Anthropic Pattern)")
    print("=" * 60)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 60)
    print("✅ Level 1 tests completed!")
    print("This tests the EXACT pattern from the Reddit user!")


if __name__ == "__main__":
    run_tests()
