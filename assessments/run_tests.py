#!/usr/bin/env python3
"""
Test Runner Script
Demonstrates how to test both candidate and model solutions.
"""

import os
import sys
import subprocess
from test_config import TEST_MODEL_SOLUTIONS, get_full_import_path

def run_tests_for_solution(solution_type, assessment_name, level):
    """Run tests for a specific solution type."""
    print(f"\n🧪 Testing {solution_type.upper()} solution for {assessment_name} {level}")
    print("=" * 60)
    
    # Set the environment variable
    env = os.environ.copy()
    if solution_type == "model":
        env['TEST_MODEL_SOLUTIONS'] = 'true'
    else:
        env['TEST_MODEL_SOLUTIONS'] = 'false'
    
    # Run pytest
    cmd = [
        sys.executable, '-m', 'pytest',
        f'{assessment_name}/{level}/',
        '--tb=no', '-q'
    ]
    
    try:
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running tests: {e}")
        return False

def main():
    """Main function to demonstrate testing both solutions."""
    print("🚀 CodeSignal Practice Repository Test Runner")
    print("=" * 60)
    
    # Example: Test banking system level 1
    assessment = "banking_system"
    level = "level1"
    
    print(f"\n📊 Current Configuration: TEST_MODEL_SOLUTIONS = {TEST_MODEL_SOLUTIONS}")
    print(f"📁 Assessment: {assessment}")
    print(f"📈 Level: {level}")
    
    # Test candidate solution
    print("\n" + "="*60)
    print("🎯 TESTING CANDIDATE SOLUTION (should fail)")
    print("="*60)
    candidate_success = run_tests_for_solution("candidate", assessment, level)
    
    # Test model solution
    print("\n" + "="*60)
    print("✅ TESTING MODEL SOLUTION (should pass)")
    print("="*60)
    model_success = run_tests_for_solution("model", assessment, level)
    
    # Summary
    print("\n" + "="*60)
    print("📋 TEST SUMMARY")
    print("="*60)
    print(f"Candidate Solution: {'❌ FAILED' if not candidate_success else '✅ PASSED'}")
    print(f"Model Solution: {'✅ PASSED' if model_success else '❌ FAILED'}")
    
    if not candidate_success and model_success:
        print("\n🎉 Perfect! This is exactly what we want:")
        print("- Candidate solutions fail (ready for practice)")
        print("- Model solutions pass (working implementations)")
    else:
        print("\n⚠️  Something needs attention:")
        print("- Candidate solutions should fail")
        print("- Model solutions should pass")

if __name__ == "__main__":
    main()
