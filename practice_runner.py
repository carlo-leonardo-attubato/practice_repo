#!/usr/bin/env python3
"""
CodeSignal Practice Runner
Guides you through speed drills and tracks progress.
"""

import os
import sys
import time
import subprocess
from pathlib import Path


class PracticeRunner:
    """Main practice runner for CodeSignal preparation."""
    
    def __init__(self):
        self.speed_drills_dir = Path("speed_drills")
        self.mock_assessments_dir = Path("mock_assessments")
        self.patterns_dir = Path("patterns")
        
    def show_menu(self):
        """Display the main practice menu."""
        print("\n" + "="*60)
        print("🚀 ANTHROPIC CODESIGNAL PRACTICE RUNNER")
        print("="*60)
        print(f"⏰ Time remaining: {self.get_time_remaining()}")
        print("\nChoose your practice session:")
        print("1. 🏃 Speed Drills (Foundation building)")
        print("2. 📝 Mock Assessments (Full practice)")
        print("3. 📚 Study Patterns (Templates & examples)")
        print("4. 📊 Progress Check (Test results)")
        print("5. 🎯 Quick Assessment (90-min simulation)")
        print("6. ❌ Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        return choice
    
    def get_time_remaining(self):
        """Calculate time remaining until assessment."""
        # Assessment is tomorrow at 2 PM PDT
        # This is a simplified calculation
        return "~18 hours"
    
    def run_speed_drills(self):
        """Run speed drill exercises."""
        print("\n🏃 SPEED DRILLS - Building Foundation")
        print("="*50)
        
        drills = [
            ("MessageStore", "message_store.py", "Basic message storage with TTL"),
            ("TTLStore", "ttl_store.py", "Key-value store with expiration"),
        ]
        
        for i, (name, file, description) in enumerate(drills, 1):
            print(f"\n{i}. {name}: {description}")
            print(f"   File: {file}")
            
            if input(f"\nRun {name} drill? (y/n): ").lower() == 'y':
                self.run_single_drill(name, file)
        
        print("\n✅ Speed drills completed!")
        input("Press Enter to continue...")
    
    def run_single_drill(self, name, filename):
        """Run a single speed drill."""
        filepath = self.speed_drills_dir / filename
        
        if not filepath.exists():
            print(f"❌ File {filename} not found!")
            return
        
        print(f"\n🎯 Running {name} drill...")
        print("="*40)
        
        # Show the file content
        with open(filepath, 'r') as f:
            content = f.read()
            print("📝 Implementation template:")
            print("-" * 30)
            print(content[:500] + "..." if len(content) > 500 else content)
            print("-" * 30)
        
        print(f"\n💡 Your task: Implement the {name} class")
        print("   Run tests when ready: python -m pytest speed_drills/test_{filename}")
        
        if input("\nReady to implement? (y/n): ").lower() == 'y':
            # Open the file for editing
            if sys.platform == "darwin":  # macOS
                subprocess.run(["open", str(filepath)])
            elif sys.platform == "win32":  # Windows
                subprocess.run(["notepad", str(filepath)])
            else:  # Linux
                subprocess.run(["nano", str(filepath)])
            
            input(f"\n📝 Edit {filename} in your editor, then press Enter to run tests...")
            
            # Run tests
            print("\n🧪 Running tests...")
            try:
                result = subprocess.run(
                    ["python", "-m", "pytest", f"speed_drills/test_{filename}", "-v"],
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    print("✅ All tests passed! Great job!")
                else:
                    print("❌ Some tests failed. Keep working!")
                    print("\nTest output:")
                    print(result.stdout)
                    print("\nErrors:")
                    print(result.stderr)
                    
            except Exception as e:
                print(f"❌ Error running tests: {e}")
    
    def run_mock_assessment(self):
        """Run a full mock assessment."""
        print("\n📝 MOCK ASSESSMENT - 90 Minute Simulation")
        print("="*50)
        print("⚠️  WARNING: This is a full 90-minute practice session!")
        print("   Set aside uninterrupted time for this.")
        
        if input("\nReady to start 90-minute assessment? (y/n): ").lower() != 'y':
            return
        
        print("\n🎯 Starting mock assessment...")
        print("⏰ Timer: 90 minutes")
        print("📋 Instructions:")
        print("   1. Read ALL levels first (5 min)")
        print("   2. Implement progressively")
        print("   3. Submit working code immediately")
        print("   4. Don't get stuck on perfection")
        
        input("\nPress Enter when ready to start timer...")
        
        # Start 90-minute countdown
        start_time = time.time()
        duration = 90 * 60  # 90 minutes in seconds
        
        while time.time() - start_time < duration:
            remaining = duration - (time.time() - start_time)
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            
            print(f"\r⏰ Time remaining: {minutes:02d}:{seconds:02d}", end="", flush=True)
            time.sleep(1)
        
        print("\n\n⏰ TIME'S UP! Assessment complete.")
        print("📊 Review your implementation and run tests.")
        input("Press Enter to continue...")
    
    def show_patterns(self):
        """Show coding patterns and templates."""
        print("\n📚 STUDY PATTERNS - Templates & Examples")
        print("="*50)
        
        patterns = [
            ("Collections Usage", "defaultdict, Counter, deque examples"),
            ("Nested Structures", "Complex nested dictionary patterns"),
            ("CRUD Operations", "Create, Read, Update, Delete patterns"),
            ("Time Operations", "Timestamp and TTL handling"),
        ]
        
        for i, (name, description) in enumerate(patterns, 1):
            print(f"{i}. {name}: {description}")
        
        print("\n💡 These patterns are essential for CodeSignal speed.")
        print("   Study them before starting drills.")
        input("\nPress Enter to continue...")
    
    def check_progress(self):
        """Check progress on speed drills."""
        print("\n📊 PROGRESS CHECK - Test Results")
        print("="*50)
        
        # Check which tests exist and run them
        test_files = list(self.speed_drills_dir.glob("test_*.py"))
        
        if not test_files:
            print("❌ No test files found. Create some first!")
            return
        
        print(f"Found {len(test_files)} test files:")
        for test_file in test_files:
            print(f"  - {test_file.name}")
        
        if input("\nRun all tests to check progress? (y/n): ").lower() == 'y':
            print("\n🧪 Running all tests...")
            try:
                result = subprocess.run(
                    ["python", "-m", "pytest", "speed_drills/", "-v"],
                    capture_output=True,
                    text=True
                )
                
                print("\nTest Results:")
                print(result.stdout)
                
                if result.stderr:
                    print("\nErrors:")
                    print(result.stderr)
                    
            except Exception as e:
                print(f"❌ Error running tests: {e}")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main run loop."""
        while True:
            choice = self.show_menu()
            
            if choice == "1":
                self.run_speed_drills()
            elif choice == "2":
                print("\n📝 Mock assessments coming soon!")
                input("Press Enter to continue...")
            elif choice == "3":
                self.show_patterns()
            elif choice == "4":
                self.check_progress()
            elif choice == "5":
                self.run_mock_assessment()
            elif choice == "6":
                print("\n👋 Good luck with your CodeSignal assessment!")
                print("Remember: Speed over perfection, working code over elegant code!")
                break
            else:
                print("\n❌ Invalid choice. Please try again.")
                input("Press Enter to continue...")


if __name__ == "__main__":
    runner = PracticeRunner()
    runner.run()
