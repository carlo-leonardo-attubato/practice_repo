import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from file_system_commands.level4.model_solution.file_system import FileSystemSimulator

class TestFileSystemLevel4:
    def test_basic_rollback(self):
        fs = FileSystemSimulator()
        
        # Upload initial file
        fs.upload_file("original.txt", "100kb")
        
        # Create a checkpoint
        checkpoint_id = fs.create_checkpoint()
        assert checkpoint_id is not None
        
        # Modify the file
        fs.upload_file("original.txt", "200kb")
        
        # Rollback to checkpoint
        result = fs.rollback_to_checkpoint(checkpoint_id)
        assert "rolled back" in result.lower()
        
        # Verify file is back to original state
        file_info = fs.get_file("original.txt")
        assert "got" in file_info
        
    def test_multiple_checkpoints(self):
        fs = FileSystemSimulator()
        
        # Upload file
        fs.upload_file("test.txt", "100kb")
        
        # Create first checkpoint
        checkpoint1 = fs.create_checkpoint()
        
        # Modify file
        fs.upload_file("test.txt", "200kb")
        
        # Create second checkpoint
        checkpoint2 = fs.create_checkpoint()
        
        # Modify file again
        fs.upload_file("test.txt", "300kb")
        
        # Rollback to first checkpoint
        fs.rollback_to_checkpoint(checkpoint1)
        file_info = fs.get_file("test.txt")
        assert "got" in file_info
        
        # Rollback to second checkpoint
        fs.rollback_to_checkpoint(checkpoint2)
        file_info = fs.get_file("test.txt")
        assert "got" in file_info
        
    def test_rollback_with_multiple_files(self):
        fs = FileSystemSimulator()
        
        # Upload multiple files
        fs.upload_file("file1.txt", "100kb")
        fs.upload_file("file2.txt", "200kb")
        
        # Create checkpoint
        checkpoint = fs.create_checkpoint()
        
        # Modify files
        fs.upload_file("file1.txt", "150kb")
        fs.upload_file("file2.txt", "250kb")
        fs.upload_file("file3.txt", "300kb")
        
        # Rollback
        fs.rollback_to_checkpoint(checkpoint)
        
        # Verify rollback
        file1_info = fs.get_file("file1.txt")
        file2_info = fs.get_file("file2.txt")
        file3_info = fs.get_file("file3.txt")
        
        assert "got" in file1_info
        assert "got" in file2_info
        assert "file not found" in file3_info  # Should not exist after rollback
        
    def test_rollback_invalid_checkpoint(self):
        fs = FileSystemSimulator()
        
        # Try to rollback to non-existent checkpoint
        result = fs.rollback_to_checkpoint("invalid_id")
        assert "not found" in result.lower()
        
    def test_checkpoint_listing(self):
        fs = FileSystemSimulator()
        
        # Create multiple checkpoints
        checkpoint1 = fs.create_checkpoint()
        checkpoint2 = fs.create_checkpoint()
        
        # List checkpoints
        checkpoints = fs.list_checkpoints()
        assert len(checkpoints) >= 2
        assert checkpoint1 in checkpoints
        assert checkpoint2 in checkpoints
