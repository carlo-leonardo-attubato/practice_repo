#!/usr/bin/env python3
"""
CodeSignal Assessment Runner
Runs progressive assessments with 4 levels each.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
import time


class AssessmentRunner:
    """Assessment runner for CodeSignal practice."""
    
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.assessments_dir = self.root_dir / "assessments"
        
    def list_assessments(self):
        """List available assessments."""
        print("🎯 Available Assessments:")
        print("="*30)
        
        for assessment_dir in self.assessments_dir.iterdir():
            if assessment_dir.is_dir():
                print(f"  📁 {assessment_dir.name}")
                
                # Check which levels exist
                levels = []
                for level in ["level1", "level2", "level3", "level4"]:
                    level_dir = assessment_dir / level
                    if level_dir.exists():
                        levels.append(level)
                
                if levels:
                    print(f"     Levels: {', '.join(levels)}")
                print()
    
    def run_assessment(self, assessment_name, mode="candidate", level=None, verbose=False, timed=False):
        """Run an assessment."""
        assessment_dir = self.assessments_dir / assessment_name
        
        if not assessment_dir.exists():
            print(f"❌ Assessment '{assessment_name}' not found!")
            return False
        
        if mode == "model":
            print(f"🧪 Testing MODEL SOLUTION: {assessment_name}")
            source_dir = "model_solution"
        else:
            print(f"🧪 Testing YOUR IMPLEMENTATION: {assessment_name}")
            source_dir = "candidate"
        
        print("="*60)
        
        # Determine which levels to run
        if level:
            levels_to_run = [level]
        else:
            levels_to_run = ["level1", "level2", "level3", "level4"]
        
        total_passed = 0
        total_tests = 0
        level_results = {}
        
        start_time = time.time() if timed else None
        
        for level_name in levels_to_run:
            level_dir = assessment_dir / level_name
            if not level_dir.exists():
                continue
            
            print(f"\n🎯 {level_name.upper()}: {self._get_level_description(level_name)}")
            print("-" * 50)
            
            level_start = time.time() if timed else None
            
            # Run tests for this level
            passed, total = self._run_level_tests(level_dir, source_dir, verbose)
            total_passed += passed
            total_tests += total
            
            level_time = time.time() - level_start if timed else None
            level_results[level_name] = {
                'passed': passed,
                'total': total,
                'time': level_time
            }
            
            if passed == total and total > 0:
                time_str = f" ({level_time:.1f}s)" if level_time else ""
                print(f"✅ {level_name.upper()}: All {total} tests PASSED!{time_str}")
            else:
                time_str = f" ({level_time:.1f}s)" if level_time else ""
                print(f"❌ {level_name.upper()}: {passed}/{total} tests passed{time_str}")
        
        total_time = time.time() - start_time if timed else None
        
        # Summary
        print(f"\n{'='*60}")
        print(f"📊 ASSESSMENT SUMMARY")
        print(f"{'='*60}")
        
        for level_name, result in level_results.items():
            status = "✅" if result['passed'] == result['total'] and result['total'] > 0 else "❌"
            time_str = f" ({result['time']:.1f}s)" if result['time'] else ""
            print(f"{status} {level_name.upper()}: {result['passed']}/{result['total']} tests{time_str}")
        
        print(f"\n🎯 TOTAL: {total_passed}/{total_tests} tests passed")
        
        if total_time:
            print(f"⏰ Total time: {total_time:.1f}s")
            if total_time > 90*60:  # 90 minutes
                print("⚠️  Over time limit! (90 minutes)")
            else:
                remaining = 90*60 - total_time
                print(f"⏰ Time remaining: {remaining/60:.1f} minutes")
        
        # Scoring estimate
        score = self._estimate_score(level_results)
        print(f"📈 Estimated score: {score}/600 points")
        
        if score >= 520:
            print("🎉 LIKELY TO PASS! (Need 520+ points)")
        else:
            print(f"💪 Need {520-score} more points to pass")
        
        return total_passed == total_tests and total_tests > 0
    
    def _get_level_description(self, level_name):
        """Get description for a level."""
        descriptions = {
            "level1": "Basic CRUD Operations (~100 pts)",
            "level2": "Enhanced Features (~150 pts)",
            "level3": "Complex Business Logic (~250 pts)",
            "level4": "Advanced Operations (~100 pts)"
        }
        return descriptions.get(level_name, "Unknown Level")
    
    def _run_level_tests(self, level_dir, source_dir, verbose):
        """Run tests for a specific level."""
        test_dir = level_dir / "tests"
        impl_dir = level_dir / source_dir
        
        if not test_dir.exists() or not impl_dir.exists():
            print(f"❌ Missing test or implementation directory")
            return 0, 1
        
        # Find test files
        test_files = list(test_dir.glob("test_*.py"))
        if not test_files:
            print(f"❌ No test files found in {test_dir}")
            return 0, 1
        
        total_passed = 0
        total_tests = 0
        
        for test_file in test_files:
            # Create temporary test file that imports from correct location
            temp_test_content = self._create_dynamic_test(test_file, impl_dir)
            temp_test_file = self.root_dir / f"temp_{test_file.stem}_{source_dir}.py"
            
            try:
                # Write temporary test file
                with open(temp_test_file, 'w') as f:
                    f.write(temp_test_content)
                
                # Run pytest
                cmd = ["python", "-m", "pytest", str(temp_test_file)]
                if verbose:
                    cmd.extend(["-v", "--tb=short"])
                else:
                    cmd.extend(["-q", "--tb=no"])
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                # Parse results
                passed, total = self._parse_test_results(result.stdout)
                total_passed += passed
                total_tests += total
                
            except Exception as e:
                print(f"❌ Error running tests: {e}")
                total_tests += 1
            finally:
                # Clean up temp file
                if temp_test_file.exists():
                    temp_test_file.unlink()
        
        return total_passed, total_tests
    
    def _create_dynamic_test(self, test_file, impl_dir):
        """Create a test file that imports from the specified implementation directory."""
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Replace the sys.path.insert line to point to the correct directory
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "sys.path.insert(0," in line and "candidate" in line:
                lines[i] = f"sys.path.insert(0, r'{impl_dir}')"
                break
        
        return '\n'.join(lines)
    
    def _parse_test_results(self, output):
        """Parse pytest output to get pass/fail counts."""
        if "FAILED" in output or "ERROR" in output:
            # Look for summary line like "1 failed, 5 passed"
            lines = output.split('\n')
            for line in lines:
                if "failed" in line and "passed" in line:
                    parts = line.split()
                    try:
                        failed_idx = next(i for i, x in enumerate(parts) if "failed" in x)
                        failed = int(parts[failed_idx-1])
                        passed_idx = next(i for i, x in enumerate(parts) if "passed" in x)
                        passed = int(parts[passed_idx-1])
                        return passed, passed + failed
                    except (ValueError, StopIteration):
                        continue
            return 0, 1  # Default if parsing fails
        elif "passed" in output:
            # All passed - look for "X passed"
            lines = output.split('\n')
            for line in lines:
                if "passed" in line and "failed" not in line:
                    parts = line.split()
                    try:
                        passed_idx = next(i for i, x in enumerate(parts) if "passed" in x)
                        passed = int(parts[passed_idx-1])
                        return passed, passed
                    except (ValueError, StopIteration):
                        continue
            return 1, 1  # Default
        else:
            return 0, 1
    
    def _estimate_score(self, level_results):
        """Estimate score based on test results."""
        score_weights = {
            'level1': 100,
            'level2': 150,
            'level3': 250,
            'level4': 100
        }
        
        total_score = 0
        for level_name, result in level_results.items():
            if result['total'] > 0:
                success_rate = result['passed'] / result['total']
                level_score = score_weights.get(level_name, 0) * success_rate
                total_score += level_score
        
        return int(total_score)
    
    def start_timed_assessment(self, assessment_name, mode="candidate"):
        """Start a timed 90-minute assessment."""
        print("⏰ TIMED ASSESSMENT MODE")
        print("="*30)
        print("You have 90 minutes to complete all levels.")
        print("Focus on Level 3 for maximum points!")
        print("\nPress Enter to start the timer...")
        input()
        
        return self.run_assessment(assessment_name, mode, timed=True)


def main():
    parser = argparse.ArgumentParser(description="CodeSignal Assessment Runner")
    parser.add_argument(
        "assessment",
        nargs="?",
        help="Assessment name (e.g., inventory_system)"
    )
    parser.add_argument(
        "--mode", 
        choices=["candidate", "model"], 
        default="candidate",
        help="Test candidate implementations or model solutions"
    )
    parser.add_argument(
        "--level",
        choices=["level1", "level2", "level3", "level4"],
        help="Run specific level only"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose test output"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true", 
        help="List available assessments"
    )
    parser.add_argument(
        "--timed", "-t",
        action="store_true",
        help="Run in timed mode (90 minutes)"
    )
    
    args = parser.parse_args()
    
    runner = AssessmentRunner()
    
    if args.list:
        runner.list_assessments()
        return
    
    if not args.assessment:
        print("❌ Please specify an assessment name or use --list to see available assessments")
        return
    
    if args.timed:
        success = runner.start_timed_assessment(args.assessment, args.mode)
    else:
        success = runner.run_assessment(args.assessment, args.mode, args.level, args.verbose)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
